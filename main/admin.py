from atexit import register
from dataclasses import field, fields
from re import I
from django.contrib import admin
from MyAccount.models import CustomUser
from .models import Vidio, Chapter
# Register your models here.
  
class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}  
    fields = (('name', 'slug'), 'description')
    
    
class VidioAdmin(admin.ModelAdmin):
    fields = ('name', 'description', ('vidio', 'privew'), 'relateed_to_chenel', ('publick','content_is_only_18_plus'), 'topik', 'vidio_for_gender')
    
admin.site.register(Vidio, VidioAdmin)
admin.site.register(Chapter, ChapterAdmin)
