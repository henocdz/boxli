import os
import re
import binascii
from time import time
from urllib import request

from django.db import models, IntegrityError
from base.models import BaseModel
from bs4 import BeautifulSoup
from helpers.math import base_convert


class Link(BaseModel):
    title = models.CharField(max_length=100, default='')
    key = models.CharField(max_length=50, unique=True, db_index=True)
    url = models.URLField(db_index=True)
    visits = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('users.User', null=True, default=None)

    class Meta:
        ordering = ['created']

    def generate_key(self):
        time_int = int(round(time() * 1000))
        key = base_convert(time_int, 62)
        return key

    def retrieve_website_title(self):
        try:
            soup = BeautifulSoup(request.urlopen(self.url), "html.parser")
        except:
            return ''
        else:
            return soup.title.string

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.title
            self.title = self.retrieve_website_title()
            while True:
                try:
                    self.key = self.generate_key()
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    pass
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
