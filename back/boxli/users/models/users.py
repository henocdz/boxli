import os
import binascii

from django.db import models
from users.models import AbstractBaseUser


class User(AbstractBaseUser):
    pass


class UserToken(models.Model):
    user = models.OneToOneField('users.User', related_name='auth_token', on_delete=models.CASCADE)
    key = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Token'
        verbose_name_plural = 'User Tokens'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
