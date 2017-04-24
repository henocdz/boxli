from rest_framework import generics
from rest_framework.exceptions import ParseError
from django.db import IntegrityError

from api.serializers.links import LinkSerializer, LinkUpdateSerializer
from api.helpers.views import CustomSerializers
from users.backends import UserTokenAuthentication
from links.models import Link


class ListCreateLinksView(generics.ListCreateAPIView):
    authentication_classes = (UserTokenAuthentication,)
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def get_owner(self):
        if self.request.auth == 'User':
            return self.request.user
        return None

    def perform_create(self, serializer):
        owner = self.get_owner()
        serializer.save(owner=owner)

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
