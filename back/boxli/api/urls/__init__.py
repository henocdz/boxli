from django.conf.urls import url, include
from api.views import root


urlpatterns = [
    url(r'^$', root.api_root, name='root'),
]
