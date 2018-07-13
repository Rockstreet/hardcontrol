from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Hard_objects, UserProfile
import nested_admin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class Hard_objectsAdmin(admin.ModelAdmin):
    model = Hard_objects

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.3.1.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.5/socket.io.min.js',
            '/static/admin/js/hardwareegistration.js',
        )




class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'




class UserAdmin(UserAdmin):
    inlines = (UserInline,)

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.3.1.min.js',
            # '//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.5/socket.io.min.js',
            '/static/admin/js/fpregistration.js',
        )





# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



admin.site.register(Hard_objects, Hard_objectsAdmin)

admin.site.site_header = "Система контроля оборудования ЭТЦП И РПРПК";
admin.site.index_title = "Вам доступны для администрирования:";
admin.site.site_title = "Система контроля оборудования ЭТЦП И РПРПК";