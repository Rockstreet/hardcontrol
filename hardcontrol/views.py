from django.conf.urls import url

from django.views import generic



from .models import Hard_objects



class Index(generic.TemplateView):
	template_name = 'hardcontrol/index.html'