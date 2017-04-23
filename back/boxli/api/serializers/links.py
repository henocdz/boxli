from rest_framework import serializers
from django.conf import settings

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    class Meta:
        model = Link
        fields = ['url', 'title', 'short_url', 'key']
        read_only_fields = ['key', 'short_url']

    def get_short_url(self, link):
        return '{}{}'.format(settings.SITE_URL, link.key)
