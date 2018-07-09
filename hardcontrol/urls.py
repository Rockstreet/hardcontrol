"""hardcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('fpregistration', views.FPregistration.as_view(), name='fpregistration'),

    path('admin/', admin.site.urls),

    path('register/', views.Register_user.as_view(), name='register_user'),

    path('hard_output/', views.hard_output, name='hard_output'),
    path('get_worker/', views.get_worker, name='get_worker'),
    path('get_worker_hard/', views.get_worker_hard, name='get_worker_hard'),
    path('get_hard_object/', views.get_hard_object, name='get_hard_object'),
    path('hard_input/', views.hard_input, name='hard_input'),
    path('list_operations/', views.ListOperations.as_view(), name='list_operations'),
    path('hard_detail/<pk>', views.HardDetail.as_view(), name='hard_detail'),
    path('worker_detail/<pk>', views.WorkerDetail.as_view(), name='worker_detail'),



]
