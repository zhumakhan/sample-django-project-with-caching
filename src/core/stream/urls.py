from django.urls import path,include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter( )
router.register(r'', StreamViewSet)

urlpatterns = [
	path('streams/', include(router.urls)),
	path('check-code/',view=CheckCodeView.as_view()),
	# path('get-new-code/',view=GetNewCodeView.as_view()),
	path('check-code-stream/',view=CheckCodeStreamView.as_view()),
	path('check-token/',view=CheckTokenView.as_view()),
]