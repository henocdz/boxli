from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import IntegrityError

from api.serializers.users import UserAuthTokenSerializer, UserCreateSerializer, UserDetailSerializer
from users.models import UserToken, User


class UserSignUpView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.create(**serializer.validated_data)
            user.set_password(password)
            user.save()
        except IntegrityError:
            return Response({'email': 'A user with this email already exists', 'type': 'email_exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = UserDetailSerializer(user, context={'request': request}).data
        response.update({'id': user.pk, 'token': self.create_token(user)})
        return Response(response)

    def create_token(self, user):
        token = UserToken.objects.create(user=user)
        return token.key


class AuthUserTokenView(APIView):
    serializer_class = UserAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = UserToken.objects.get_or_create(user=user)
        return Response({'token': token.key, 'pk': user.pk,
                         'email': user.email, 'first_name': user.first_name})

