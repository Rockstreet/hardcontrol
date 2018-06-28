from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Hard_objects
import nested_admin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Hard_objectsAdmin(admin.ModelAdmin):
    model = Hard_objects



admin.site.register(Hard_objects, Hard_objectsAdmin)

admin.site.site_header = "Система контроля оборудования ЭТЦП И РПРПК";
admin.site.index_title = "Вам доступны для администрирования:";
admin.site.site_title = "Система контроля оборудования ЭТЦП И РПРПК";