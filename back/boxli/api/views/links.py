from rest_framework import generics
from rest_framework.exceptions import ParseError
from django.db import IntegrityError

from api.serializers.links import LinkSerializer
from api.helpers.views import CustomSerializers
from links.models import Link


class ListCreateLinksView(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def create(self, *args, **kwargs):
        try:
            return super().create(*args, **kwargs)
        except IntegrityError:
            raise ParseError({'key': 'That key already exist'})
