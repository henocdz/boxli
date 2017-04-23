from django.shortcuts import redirect
from django.views.generic import View
from django.http import Http404
from links.models import Link

# Create your views here.
class RedirectLinkView(View):
    def get(self, request, key, *args, **kwargs):
        try:
            link = Link.objects.get(key=key)
        except Link.DoesNotExist:
            raise Http404()
        else:
            return redirect(link.url)
