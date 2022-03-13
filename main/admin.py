from atexit import register
from re import I
from django.contrib import admin
from MyAccount.models import CustomUser
from .models import Vidio
# Register your models here.
  

admin.site.register(Vidio)
