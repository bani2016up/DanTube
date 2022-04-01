from dataclasses import fields
from pyexpat import model
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Vidio


class AddVidioForm(forms.Form):
    model = Vidio
    fields =  ('name', 'description', 'vidio', 'privew', 'publick', 'content_is_only_18_plus', 'topik')
    