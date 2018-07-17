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

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout



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

        context['hardtransaction_list'] = HardTransaction.objects.filter(hard_id=self.object.pk).order_by('-datetime')

        return context


class WorkerDetail(generic.DetailView):
    model = User
    template_name = 'hardcontrol/worker_detail.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerDetail, self).get_context_data(**kwargs)

        context['hard_on_worker'] = HardOnWorker.objects.filter(worker_id=self.object.pk)

        context['worker']=context['user']

        context['user'] = manager_id=self.request.user

        context['hardtransaction_list'] = HardTransaction.objects.filter(worker_id=self.object.pk).order_by('-datetime')

        return context

class HardList(generic.ListView):
    model = Hard_objects
    template_name = 'hardcontrol/hard_list.html'

    def get_queryset(self):
        try:
            title = self.request.GET['title']
        except:
            title = ''
        if (title != ''):
            object_list = self.model.objects.filter(title__icontains=title)

        else:
            object_list = self.model.objects.all()
        return object_list


class WorkerList(generic.ListView):
    model = User
    template_name = 'hardcontrol/worker_list.html'

    def get_queryset(self):
        try:
            name = self.request.GET['last_name']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(last_name__icontains=name)

        else:
            object_list = self.model.objects.all()
        return object_list



class LoginPage(generic.View):


    template_name = 'hardcontrol/login_page.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'form': 'form'})


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)



        if user is not None:
                if user.groups.filter(name__in=['Менеджеры выдачи']).exists():
                    login(request, user)
                    return HttpResponseRedirect('/')

        return render(request, self.template_name, {'error': 'Неверный Логин или Пароль'})







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

    hard_transaction=HardTransaction(type=True, worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id),manager_id=request.user)
    hard_transaction.save()

    hard_on_worker=HardOnWorker(worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id),manager_id=request.user)
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
        select_auto = request.GET['select_auto']

    if select_auto=='1':
        select_auto=True
    else:
        select_auto=False


    hard_object = Hard_objects.objects.get(pk=hard_id)
    hard_object.status = True
    hard_object.save()

    hard_transaction = HardTransaction(type=False, worker_id=User.objects.get(pk=worker_id),
                                       hard_id=Hard_objects.objects.get(pk=hard_id), manager_id=request.user, select_auto=select_auto);
    hard_transaction.save()

    hard_on_worker = HardOnWorker.objects.filter(hard_id=Hard_objects.objects.get(pk=hard_id)).delete()

    return HttpResponse(hard_id)

def exit(request):

    logout(request)

    return HttpResponseRedirect('/login_page/')

