from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        return super().get(request, *args, **kwargs)