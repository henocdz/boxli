from django.shortcuts import redirect
from django.views.generic import View
from django.http import Http404
from django.db.models import F

from links.models import Link

# Create your views here.
class RedirectLinkView(View):
    def get(self, request, key, *args, **kwargs):
        try:
            links = Link.objects.filter(key=key)
            link = links[0]
            links.update(visits=F('visits') + 1)
        except Link.DoesNotExist:
            raise Http404()
        else:
            return redirect(link.url)
