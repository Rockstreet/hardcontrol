from django.conf.urls import url

from django.views import generic

from django.contrib.auth.models import User

from .models import UserProfile

from django.views.generic import CreateView


from .models import Hard_objects



class Index(generic.TemplateView):
	template_name = 'hardcontrol/index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		context['hardw_list']=Hard_objects.objects.filter(status=True).all



		return context






class Register_user(generic.CreateView):

	model = User

	fields = ['username']

	template_name = 'hardcontrol/register_user.html'


	def createuser(request):

		user = User.objects.create_user(
			username=request.POST.cleaned_data['username'],
			email=request.POST.cleaned_data['email'],
			password=request.POST.cleaned_data['password1']
		)
		user.save()
		user_profile=UserProfile.objects.create(
			user=user,
			passport=request.POST.cleaned_data['username'],
		)
		user_profile.save()


		return True