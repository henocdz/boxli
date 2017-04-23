from rest_framework import serializers
from django.conf import settings

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'url', 'title', 'short_url', 'key']
        read_only_fields = ['id', 'key', 'short_url']

    def get_short_url(self, link):
        return '{}{}'.format(settings.SITE_URL, link.key)


class LinkUpdateSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'url',  'short_url', 'key', 'created', 'title']
        read_only_fields = ['id', 'created', 'url', 'title']

    def get_short_url(self, link):
        return '{}{}'.format(settings.SITE_URL, link.key)

