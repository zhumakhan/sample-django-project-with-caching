
from django.urls import path,include
from rest_framework import routers

from .views import *

urlpatterns = [
	path('cloudpayment-notification-check/',view=cloudpayment_notification_check),
	path('cloudpayment-notification-pay/',view=cloudpayment_notification_pay),
	path('cloudpayment-notification-fail/',view=cloudpayment_notification_fail),
	path('cloudpayment-notification-confirm/',view=cloudpayment_notification_confirm),
	path('cloudpayment-notification-refund/',view=cloudpayment_notification_refund),
	path('cloudpayment-notification-cancel/',view=cloudpayment_notification_cancel),
	path('buy-ticket/',view=BuyTicketView.as_view()),

]
