from django.db import models
from base.models import BaseModel


class Link(BaseModel):
    title = models.CharField(max_length=100, default='')
    key = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.title
