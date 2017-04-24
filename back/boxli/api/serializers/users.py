from rest_framework import serializers

from users.models import User, UserToken


class UserAuthTokenSerializer(serializers.Serializer):
    """Parses a phone and an email and returns a token for authenticating
    requests of `User` instances.
    """
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = self.authenticate(email=email, password=password)

            if user is None:
                msg = 'Combination of password and email is invalid'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

    def authenticate(self, email, password):
        try:
            user = User.objects.get(email=email.strip()) # help s out by removing whitespace from email
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password', 'id']
        read_only_fields = ['id']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'id']
        read_only_fields = ['first_name', 'email', 'id']
