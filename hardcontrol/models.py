from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

from sorl.thumbnail import ImageField

class Hard_objects(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)
    title = models.CharField(_("Наименование оборудования"), max_length=1000, default='')
    rfid_id = models.CharField(_("Rfid ID"), max_length=1000, default='')
    meta_description = models.CharField(_("Описание оборудования"), max_length=1000, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Оборудование")
        verbose_name_plural = _("Оборудование")
        ordering = ['title', ]





class UserProfile(models.Model):

    user = models.OneToOneField(User,related_name='related_name_user', on_delete=models.CASCADE)
    foto = models.ImageField(_("Фото"),upload_to='images/users', blank=True)
    passport = models.CharField(_("Номер паспорта"), max_length=1000, default='', blank=True)
    template1 = models.TextField(null=True, blank=True)
    template2 = models.TextField(null=True, blank=True)
    template3 = models.TextField(null=True, blank=True)
    template4 = models.TextField(null=True, blank=True)
    template5 = models.TextField(null=True, blank=True)
    template6 = models.TextField(null=True, blank=True)
    template7 = models.TextField(null=True, blank=True)
    template8 = models.TextField(null=True, blank=True)
    template9 = models.TextField(null=True, blank=True)
    template10 = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

