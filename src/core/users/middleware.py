from datetime import date

from django.contrib.auth import get_user_model

import json
from re import sub

from rest_framework.authtoken.models import Token

from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .expiring_token_authentication import token_expire_handler


User = get_user_model()


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
            is_expired, token = token_expire_handler(token)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        if User.is_authenticated:
            User.objects.filter(id=token.user.id).update(last_active=timezone.now())

        if is_expired and User.is_authenticated:
            raise AuthenticationFailed("The Token is expired")

        return token.user, token


