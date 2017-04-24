from django.conf.urls import url, include
from api.views import users


urlpatterns = [
    url(r'^signup/$', users.UserSignUpView.as_view(), name='signup'),
    url(r'^auth/$', users.AuthUserTokenView.as_view(), name='auth'),
]
