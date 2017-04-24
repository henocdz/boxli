from django.conf.urls import url, include
from api.views import root


urlpatterns = [
    url(r'^$', root.api_root, name='root'),
    url(r'^links/', include('api.urls.links', namespace='links')),
    url(r'^users/', include('api.urls.users', namespace='users')),
]
