from django.conf.urls import url

from django.http import HttpResponse,JsonResponse

from django.views import generic

from django.contrib.auth.models import User

from .models import UserProfile, Hard_objects, HardOnWorker, HardTransaction

from django.views.generic import CreateView

from django.core.serializers.json import DjangoJSONEncoder

from django.core import serializers

import json

from .models import Hard_objects



class Index(generic.TemplateView):
	template_name = 'hardcontrol/index.html'


	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		context['hardw_list']=Hard_objects.objects.filter(status=True).all


		context['worker_list']=User.objects.filter(groups__name='Сотрудники')

		print(context['worker_list'])


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


class ListOperations(generic.ListView):


    model = HardTransaction
    ordering = ['-datetime']
    template_name = 'hardcontrol/list_operations.html'

    def get_context_data(self, **kwargs):
        context = super(ListOperations, self).get_context_data(**kwargs)
        return context

class HardDetail(generic.DetailView):

    model = Hard_objects
    template_name = 'hardcontrol/hard_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HardDetail, self).get_context_data(**kwargs)

        if self.object.status==False:
            context['this_worker'] = HardOnWorker.objects.filter(hard_id=self.object.pk).last().worker_id
            context['this_worker_data'] = HardOnWorker.objects.filter(hard_id=self.object.pk).last().datetime






        return context






class FPregistration(generic.TemplateView):
	template_name = 'hardcontrol/fpregistration.html'


def hard_output(request):
    hard_id = None
    if request.method == 'GET':
        hard_id = request.GET['hard_id']
        worker_id =  request.GET['worker_id']

    hard_object=Hard_objects.objects.get(pk=hard_id)
    hard_object.status=False
    hard_object.save()

    hard_transaction=HardTransaction(type=True, worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id));
    hard_transaction.save()

    hard_on_worker=HardOnWorker(worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id))
    hard_on_worker.save()



    return HttpResponse(hard_id)

def get_worker(request):
    worker_id = None
    if request.method == 'GET':
        worker_id =  request.GET['worker_id']
    worker=User.objects.get(pk=worker_id)

    s = serializers.serialize('json', [worker])
    # s is a string with [] around it, so strip them off
    worker_obj = s.strip("[]")


    return HttpResponse(worker_obj)

def get_worker_hard(request):
    worker_id = None
    if request.method == 'GET':
        worker_id = request.GET['worker_id']
    worker = User.objects.get(pk=worker_id)



    hard_objects=HardOnWorker.objects.filter(worker_id=worker)

    s = serializers.serialize('json', hard_objects)

    print(hard_objects)

    #structure= s.strip("[]")

    return HttpResponse(s)


def get_hard_object(request):
    hard_id = None
    if request.method == 'GET':
        hard_id =  request.GET['hard_id']
    hard=Hard_objects.objects.get(pk=hard_id)

    s = serializers.serialize('json', [hard])

    hard_obj = s.strip("[]")


    return HttpResponse(hard_obj)


def hard_input(request):
    hard_id = None
    if request.method == 'GET':
        hard_id = request.GET['hard_id']
        worker_id = request.GET['worker_id']

    hard_object = Hard_objects.objects.get(pk=hard_id)
    hard_object.status = True
    hard_object.save()

    hard_transaction = HardTransaction(type=False, worker_id=User.objects.get(pk=worker_id),
                                       hard_id=Hard_objects.objects.get(pk=hard_id));
    hard_transaction.save()

    hard_on_worker = HardOnWorker.objects.filter(hard_id=Hard_objects.objects.get(pk=hard_id)).delete()

    return HttpResponse(hard_id)

