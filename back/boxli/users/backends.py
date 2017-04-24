from time import time

from django.contrib.auth.models import User
from django.conf import settings
from django.core import signing

from rest_framework import authentication
from rest_framework import exceptions

from users.models import UserToken, User


class UserTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION') # get auth token from header
        if not token:
            return None

        auth_type, token = token.split(' ')
        try:
            tkn = UserToken.objects.get(key=token)
        except UserToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('invalid_token')
        return (tkn.user, 'User')

