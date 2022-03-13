from django.contrib import admin
from .models import CustomUser
# Register your models here.
class ChneleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Chenelname',)}  
admin.site.register(CustomUser, ChneleAdmin)