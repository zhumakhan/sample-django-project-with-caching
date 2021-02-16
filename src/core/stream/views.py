

from django.core.cache import cache
from django.utils.crypto import get_random_string

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework import viewsets, filters,status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# from coolname import generate_slug

from ..helpers.task_email import send_async_email
from ..helpers.constants import CACHE_TIMEOUT
from ..helpers.max_allowed_requests import attempts

from .serializers import *
from .models import *
from .filters import *

class StreamViewSet(viewsets.ModelViewSet):
	serializer_class = StreamSerializer
	queryset = Stream.objects.all()
	# permission_classes = (AllowAny,)
	filter_backends = [filters.OrderingFilter,DjangoFilterBackend]
	filterset_class = StreamFilter
	def get_permissions(self):
		permission_classes = []
		if self.action in ('list', 'retrieve',):
			permission_classes = [AllowAny]
		elif self.action in ('create', 'update', 'partial_update'):
			permission_classes = [IsAdminUser]
		elif self.action in ('destroy',):
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]


class CheckCodeStreamView(GenericAPIView):
	serializer_class = CheckCodeStreamSerializer
	permission_classes = (AllowAny,)
	def post(self,request,*args,**kwargs):
		
		tries = attempts(request,4,60)
		
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		code = serializer.validated_data.get('code')
		stream_id = serializer.validated_data.get('stream_id')
		
		code_object = Code.objects.filter(code=code,stream_id=stream_id,valid=True)
		if tries >= 0 and code_object:
			token = get_random_string(length=10)
			prev_token = cache.get(code)
			if prev_token:
				cache.delete(prev_token)
			cache.set(code,token,CACHE_TIMEOUT)
			cache.set(token,1,CACHE_TIMEOUT)
			res={"message":"OK","tries":tries,"token": token}
			s=status.HTTP_200_OK
		else:
			res={"message":"Not Found.","tries":max(0,tries)}
			s=status.HTTP_404_NOT_FOUND

		return Response(res,status=s)

class CheckCodeView(GenericAPIView):
	serializer_class = CheckCodeSerializer
	permission_classes = (AllowAny,)
	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		code = serializer.validated_data.get('code')
		code_object = None
		code_object = Code.objects.filter(code=code,valid=True)
		if code_object:
			stream_id = code_object[0].stream.id
			token = get_random_string(length=10)
			prev_token = cache.get(code)
			if prev_token:
				cache.delete(prev_token)
			cache.set(code,token,CACHE_TIMEOUT)
			cache.set(token,1,CACHE_TIMEOUT)
			# code_object.update(valid=False)
			return Response({"message":"OK","token": token,"stream_id":stream_id},status=status.HTTP_200_OK)
		else:
			return Response({"message":"Not Found."},status=status.HTTP_404_NOT_FOUND)


class CheckTokenView(GenericAPIView):
	serializer_class = CheckTokenSerializer
	permission_classes = (AllowAny,)
	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		token = serializer.validated_data.get('token')
		if cache.get(token):
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)






