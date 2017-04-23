import os
import binascii

from django.db import models, IntegrityError
from base.models import BaseModel


class Link(BaseModel):
    title = models.CharField(max_length=100, default='')
    key = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    class Meta:
        ordering = ['created']

    def generate_key(self):
        return binascii.hexlify(os.urandom(3)).decode()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.title
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
