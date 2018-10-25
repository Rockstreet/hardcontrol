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

from urllib.parse import urlencode

import base64
from django.db.models import Q


class Index(generic.TemplateView):
	template_name = 'hardcontrol/index.html'


	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		context['hardw_list']=Hard_objects.objects.filter(status=True).filter(repair=False).all


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
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListOperations, self).get_context_data(**kwargs)
        context['all_managers'] = User.objects.filter(groups__name='Менеджеры выдачи')

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = urlencode(query_params)

        return context

    def get_queryset(self):

            object_list = self.model.objects.all().order_by('-datetime')

            try:
                title = self.request.GET['title']
            except:
                title = ''

            try:
                last_name = self.request.GET['last_name']
            except:
                last_name = ''

            try:
                type = self.request.GET['type']
            except:
                type = ''

            try:
                date_ot = self.request.GET['date_ot']
            except:
                date_ot = ''

            try:
                date_po = self.request.GET['date_po']
            except:
                date_po = ''

            try:
                select_auto = self.request.GET['select_auto']
            except:
                select_auto = ''

            try:
                manager = self.request.GET['manager']
            except:
                manager = ''

            try:
                name = self.request.GET['name']
            except:
                name = ''


            if (manager != 'Все' and manager !='') :
                object_list = object_list.filter(manager_id=manager).order_by('-datetime')


            if (select_auto == '1'):
                object_list = object_list.filter(select_auto=True).order_by('-datetime')

            if (select_auto == '0'):
                object_list = object_list.filter(select_auto=False).order_by('-datetime')


            if (date_po != ''):
                object_list = object_list.filter(datetime__lte=date_po).order_by('-datetime')



            if (date_ot != ''):
                object_list = object_list.filter(datetime__gte=date_ot).order_by('-datetime')

            if (type == '1'):
                object_list = object_list.filter(type=True).order_by('-datetime')

            if (type == '0'):
                object_list = object_list.filter(type=False).order_by('-datetime')


            if (last_name != ''):
                object_list = object_list.filter(worker_id__last_name__icontains=last_name).order_by('-datetime')


            if (title != ''):
                object_list = object_list.filter(hard_id__title__icontains=title).order_by('-datetime')

            if (name != ''):
                object_list = object_list.filter(hard_id__name__icontains=name).order_by('-datetime')


            return object_list







class HardDetail(generic.DetailView):

    model = Hard_objects
    template_name = 'hardcontrol/hard_detail.html'

    def plural_for_number(self, number):
        text = "раз"
        n10 = abs(number) % 10
        n100 = abs(number) % 100
        if ((n10 == 2) or (n10 == 3) or (n10 == 4)):
            text = "раза"
            if ((n10 == 2) or (n10 == 3) or (n10 == 4)):
                if ((n100 > 10) and (n10 < 20)):
                    text = "раз"
                else:
                    text = "раза"
            else:
                text = "раз"

        return text

    def get_context_data(self, **kwargs):
        context = super(HardDetail, self).get_context_data(**kwargs)

        if self.object.status==False:
            context['this_worker'] = HardOnWorker.objects.filter(hard_id=self.object.pk).last().worker_id
            context['this_worker_data'] = HardOnWorker.objects.filter(hard_id=self.object.pk).last().datetime

        context['hardtransaction_list'] = HardTransaction.objects.filter(hard_id=self.object.pk).order_by('-datetime')

        hardtransaction_used = HardTransaction.objects.filter(hard_id=self.object.pk, type=True).count()
        context['hardtransaction_used'] = hardtransaction_used
        context['hardtransaction_used_text'] = self.plural_for_number(hardtransaction_used)

        return context


class WorkerDetail(generic.DetailView):
    model = User
    template_name = 'hardcontrol/worker_detail.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerDetail, self).get_context_data(**kwargs)

        context['hard_on_worker'] = HardOnWorker.objects.filter(worker_id=self.object.pk)

        context['worker']=context['user']

        context['user'] = manager_id=self.request.user

        context['profile'] = UserProfile.objects.filter(user=context['worker']).first()

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
            object_list = self.model.objects.filter(Q(title__contains=title) | Q(meta_description__contains=title) | Q(name__contains=title))

        else:
            object_list = self.model.objects.all()

        return object_list

    def get_context_data(self, **kwargs):
        context = super(HardList, self).get_context_data(**kwargs)

        context['object_list_used'] = {}
        for v in context['object_list']:
            context['object_list_used'][v.pk] = (HardTransaction.objects.filter(hard_id=v.pk, type=True).count())

        return context




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
        select_auto = request.GET['select_auto']

    if select_auto == '1':
        select_auto = True
    else:
        select_auto = False



    hard_object=Hard_objects.objects.get(pk=hard_id)
    hard_object.status=False
    hard_object.save()

    hard_transaction=HardTransaction(type=True, worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id),manager_id=request.user, select_auto=select_auto)
    hard_transaction.save()

    hard_on_worker=HardOnWorker(worker_id=User.objects.get(pk=worker_id), hard_id=Hard_objects.objects.get(pk=hard_id),manager_id=request.user, select_auto=select_auto)
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


def get_worker_photo(request):

    if request.method == 'GET':
        worker_id =  request.GET['worker_id']
    try:
        photo_url = UserProfile.objects.filter(user=worker_id).first().foto.url
    except:
        photo_url=''


    return HttpResponse(photo_url)



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


def hard_complect(request):

    if request.method == 'GET':
        hard_id =  request.GET['hard_id']

    hardObj = Hard_objects.objects.filter(pk=hard_id).first()
    
    hard_complect = ''
    # hard_complect+= '<b>Серийный номер:</b> ' + hardObj.number1 + '<br>' if hardObj.number1 != '' else ""
    hard_complect+= '<b>Инвентарный номер:</b> ' + hardObj.number1 + '<br>' if hardObj.number1 != '' else ""
    hard_complect+= '<b>Заводской номер:</b> ' + hardObj.number2 + '<br>' if hardObj.number2 != '' else ""
    hard_complect+= '<b>Наименование инженерно-технического средства:</b> ' + hardObj.name + '<br>' if hardObj.name != '' else ""
    hard_complect+= '<b>Наименование ремонтных комплектов:</b> ' + hardObj.name_rem + '<br>' if hardObj.name_rem != '' else ""
    hard_complect+= '<b>Номер свидетельства о регистрации:</b> ' + hardObj.number_reg + '<br>' if hardObj.number_reg != '' else ""
    hard_complect+= '<b>Марка транспортного средства:</b> ' + hardObj.number_name + '<br>' if hardObj.number_name != '' else ""
    hard_complect+= '<b>№ паспорта:</b> ' + hardObj.dop_1 + '<br>' if hardObj.dop_1 != '' else ""
    hard_complect+= '<b>№ удостоверения:</b> ' + hardObj.dop_2 + '<br>' if hardObj.dop_2 != '' else ""
    hard_complect+= '<b>Денежные средства:</b> ' + hardObj.dop_3 + '<br>' if hardObj.dop_3 != '' else ""
    hard_complect+= '<b>Вид и номер носильных МТС:</b> ' + hardObj.dop_4 + '<br>' if hardObj.dop_4 != '' else ""
    hard_complect+= '<b>Описание оборудования:</b> ' + hardObj.meta_description + '<br>' if hardObj.meta_description != '' else ""

    hard_complect+= '<b>Комплектность:</b><br>' + hardObj.complect.replace('\n', '<br />') + '<br>' if hardObj.complect != '' else ""

    return HttpResponse(hard_complect)