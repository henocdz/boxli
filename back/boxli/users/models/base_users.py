from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser as DjAbstractBaseUser
from django.utils.translation import ugettext as _
from django.contrib.auth.models import PermissionsMixin


from users.manager import UserManager


class AbstractBaseUser(DjAbstractBaseUser):
    """Defines common attributes among Boxli User Types"""
    email = models.EmailField(unique=True, db_index=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=100, db_index=True, verbose_name=_('First Name'))
    surname = models.CharField(max_length=140, db_index=True, verbose_name=_('Surname'))
    is_active = models.BooleanField(default=True)
    join_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Join Date'))
    last_edit_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    class Meta:
        # This model should not be created in the database
        abstract = True

    def get_short_name(self): # required to avoid a `NotImplementedError` for subclasses of `AbstractBaseUser`
        return self.first_name.capitalize()

    @property
    def is_staff(self):
        return False

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return "{email}".format(email=self.email)


class AdminUser(AbstractBaseUser, PermissionsMixin):
    @property
    def is_staff(self):
        return True
