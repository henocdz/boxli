import os
import re
import binascii
from urllib import request

from django.db import models, IntegrityError
from base.models import BaseModel
from bs4 import BeautifulSoup


class Link(BaseModel):
    title = models.CharField(max_length=100, default='')
    key = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    class Meta:
        ordering = ['created']

    def generate_key(self):
        regex = re.compile('')
        key = binascii.hexlify(os.urandom(3)).decode()
        # make sure that there is at least one non-digit in the key
        while not re.search('\D', key, re.IGNORECASE):
            key = binascii.hexlify(os.urandom(3)).decode()
        return key

    def retrieve_website_title(self):
        try:
            soup = BeautifulSoup(request.urlopen(self.url))
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
