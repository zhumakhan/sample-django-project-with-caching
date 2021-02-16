import hashlib
import hmac
import base64
import requests
import json
import pytz

from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from coolname import generate_slug

from core.stream.models import Code,Stream
from ..helpers.task_email import send_async_email
from ..helpers.local_time import LOCAL_TIME_ZONE
from .serializers import *
from .tasks import send_check_to_email

secret = bytes(settings.C_API_SECRET, 'utf-8')
basicauth_code = base64.b64encode(bytes(settings.C_PUBLIC_ID + ':'+settings.C_API_SECRET,'utf-8')).decode("ascii")
# message = bytes('Message', 'utf-8')
# signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
# print(signature)

class BuyTicketView(GenericAPIView):
	serializer_class = BuyTickerSerializer
	permission_classes = (AllowAny,)
	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(data=request.data,context={'context':request})
		serializer.is_valid(raise_exception=True)
		email = serializer.validated_data.get('email')
		stream_id = serializer.validated_data.get('stream_id')
		try:
			stream = Stream.objects.get(id=stream_id)
			buy_tickt_body = {
				'Amount': stream.ticket_cost,
				"Currency":stream.currency,
				"Description":"Купить билеты на стрим / By tickets for stream",
				"Email":email,
				"InvoiceId":stream_id,
				"RequireConfirmation":True,
				"SendEmail":True,
			}
			send_check_to_email.delay(url=settings.C_CREATE_EMAIL_CHECK_URL,
	    		# params={'q': 'requests+language:python'},
	    		headers={'Accept': 'application/json','Authorization':'Basic '+basicauth_code},
				data=buy_tickt_body)
			# resp_body = json.loads(response.content)
			# if resp_body.get("Success"):
			# 	return Response({'message':'OK'},status=status.HTTP_200_OK)
			# else:
			# 	return Response({'message':resp_body.get("Message")},status=status.HTTP_400_BAD_REQUEST)
			return Response({'message':'OK'},status=status.HTTP_200_OK)
		except Stream.DoesNotExist:
			return Response({'message':'Stream not found'},status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			print(e)
			return Response({'message':'Internal server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_pay(request):
	#check if host is cloudpayment
	signature = base64.b64encode(hmac.new(secret, request.body, digestmod=hashlib.sha256).digest()).decode("utf-8")
	if signature != request.headers.get('Content-Hmac'):
		# print("HOST IS NOT VALID")
		return Response({"code":0})
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	try:
		stream = Stream.objects.get(id=invoice_id)
		try:
			attempts=10
			while attempts > 0:
				attempts-=1
				code = get_random_string(length=5)
				if not Code.objects.filter(code=code,stream_id=invoice_id).exists():
					Code.objects.create(code=code,stream_id=invoice_id,email=email)
					attempts=-10
			if attempts != -10:
				raise Exception("Sorry, can't create random code")
		except Exception as e:
			print(e)
			send_async_email.delay([email],'Stream code','Some errors happened, please contact manager or try later')
		else:
			msg_html = render_to_string('email_code.html', {'code': code,'title':stream.title})
			send_async_email.delay([email],'Поздравляем! Вы купили билет на концерт!','Билет: '+code, html_message=msg_html)
	except Stream.DoesNotExist:
		send_async_email.delay([email],'Stream code','Some errors happened, please contact manager or try later')
	except:
		send_async_email.delay([email],'Stream code','Some errors happened, please contact manager or try later')
	return Response({"code": 0})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_check(request):
	now = datetime.now().astimezone(LOCAL_TIME_ZONE)
	#check if host is cloudpayment
	signature = base64.b64encode(hmac.new(secret, request.body, digestmod=hashlib.sha256).digest()).decode("utf-8")
	if signature != request.headers.get('Content-Hmac'):
		print("HOST IS NOT VALID")
		return Response({"code":13})
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	currency = request.data.get('Currency')
	amount = request.data.get('Amount')
	try:
		stream = Stream.objects.get(id=invoice_id)
		if not currency or not amount or currency != stream.currency or float(amount) != stream.ticket_cost:
			print("AMOUNT")
			print(currency,amount,stream.currency,stream.ticket_cost)
			print(type(currency),type(amount),type(stream.currency),type(stream.ticket_cost))
			return Response({"code": 12})#wrong amount
		elif stream.end_time and stream.end_time <= now:
			print("TIME")
			print(stream.end_time)
			print(now)
			return Response({"code": 20})#payment expired
		elif len(email) == 0:
			print('EMAIL')
			print(email)
			return Response({"code":13})#payment can't be made, no email, for our case we do not need it
		else:
			print("SUCCESS")
			return Response({"code": 0})#payment can be made
	except Stream.DoesNotExist:
		print("STREAM DOES NOT EXIST")
		return Response({"code": 10})#wrong order number, stream id does not exist
	except Exception as e:
		print(e)
		print("UNKNOWN EXCEPTION")
		return Response({"code":13})#payment can't be made
	print("LAST LINE")
	return Response({"code":13})#payment can't be made


@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_fail(request):
	print("FAIL")
	print(request.data)
	print(request.headers)
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	return Response({"code": 0})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_confirm(request):
	print("CONFIRM")
	print(request.data)
	print(request.headers)
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	return Response({"code": 0})

@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_refund(request):
	print("REFUND")
	print(request.data)
	print(request.headers)
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	return Response({"code": 0})

@api_view(['POST'])
@permission_classes((AllowAny, ))
def cloudpayment_notification_cancel(request):
	print("CANCEL")
	print(request.data)
	print(request.headers)
	email = request.data.get('Email')
	invoice_id = request.data.get('InvoiceId')
	return Response({"code": 0})


