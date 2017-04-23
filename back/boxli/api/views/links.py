from rest_framework import generics
from rest_framework.exceptions import ParseError
from django.db import IntegrityError

from api.serializers.links import LinkSerializer, LinkUpdateSerializer
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


class RetrieveUpdateLinkView(generics.RetrieveUpdateAPIView):
    serializer_class = LinkUpdateSerializer
    queryset = Link.objects.all()

    def perform_update(self, serializer):
        key = serializer.validated_data['key']
        link = self.get_object()
        if link.key == key:
            serializer.save()
            return
        if Link.objects.filter(key=key).exists():
            raise ParseError({'key': 'That key already exist'})
        serializer.save()
