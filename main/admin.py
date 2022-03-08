from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.
    
class ChneleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}   
admin.site.register(Vidio)
admin.site.register(Chenele, ChneleAdmin)