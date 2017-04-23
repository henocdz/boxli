from django.conf.urls import url, include
from api.views import links


urlpatterns = [
    url(r'^$', links.ListCreateLinksView.as_view(), name='list-create'),
    url(r'^(?P<pk>\d+)/$', links.RetrieveUpdateLinkView.as_view(), name='retrieve-update')
]
