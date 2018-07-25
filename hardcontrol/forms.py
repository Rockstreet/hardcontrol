from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from django.forms import ModelForm
from .models import UserProfile


class CreateAccountForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("username","password","password2","first_name","last_name",
                  "gender","medication","medical_history","DOB","email","telephone",
                  "address","city","state","postcode")






