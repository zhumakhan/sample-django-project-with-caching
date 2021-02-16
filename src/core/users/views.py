from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CRMAuthTokenSerializer,UserSerializer
from .expiring_token_authentication import token_expire_handler,expires_in

User = get_user_model()

class ObtainAuthToken(GenericAPIView):
	serializer_class = CRMAuthTokenSerializer
	permission_classes = (AllowAny,)
	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data.get('user')
		Token.objects.filter(user=user).delete()
		token = Token.objects.create(user=user)
		user.last_active = timezone.now()
		is_expired,token = token_expire_handler(token)
		user.user_last_login = timezone.now()
		user.save()
		return Response(
			{'token':token.key,'expires_in':expires_in(token),'user':UserSerializer(user).data}
		)

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)
	filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
	filterset_fields = ['id']
	search_fields = ['^email','^full_name']
	# def get_permissions(self):
 #        permission_classes = []
 #        if self.action in ('list', 'retrieve',):
 #            permission_classes = [AllowAny]
 #        elif self.action in ('create', 'update', 'partial_update'):
	# 		permission_classes = [IsAdminUser]
 #        elif self.action in ('destroy',):
 #            permission_classes = [IsAdminUser]
 #        return [permission() for permission in permission_classes]