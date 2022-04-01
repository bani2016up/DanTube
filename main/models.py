from audioop import reverse
from multiprocessing.spawn import old_main_modules
from statistics import mode
from django.db import models
from django.core.validators import FileExtensionValidator
from MyAccount.models import CustomUser

# Create your models here.
class Vidio(models.Model):
    GENDER = (
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Other', 'Other'),
        )
    
    name = models.CharField(max_length=115)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    vidio = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mkv'])])
    privew = models.FileField(upload_to='media/')
    relateed_to_chenel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publick = models.BooleanField(default=True)
    watched = models.BigIntegerField(default=False)
    topik = models.ManyToManyField('Chapter')
    content_is_only_18_plus = models.BooleanField(default=False)
    vidio_for_gender = models.CharField(choices=GENDER, default='Other', max_length=8)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def find_gender(self):
        if 'game' in self.name:
            for_gender = 'Man'
        elif 'Test' in self.name:
            for_gender = 'Woman'
        else:
            for_gender = 'Other'
        return for_gender

class Chapter(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, max_length=40, db_index=True)
    description = models.CharField(max_length=1028)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"Chapter_slug": self.slug})
    



