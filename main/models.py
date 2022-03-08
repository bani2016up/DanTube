from audioop import reverse
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Vidio(models.Model):
    name = models.CharField(max_length=115)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    vidio = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov'])])
    privew = models.FileField(upload_to='media/')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


class Chenele(models.Model):
    
    name = models.CharField(max_length=32)
    datecreated = models.DateField(auto_now_add=True)
    icon = models.ImageField()
    backgtound = models.ImageField()
    descprion = models.TextField()
    vidio = models.ManyToManyField(Vidio)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Chenele", kwargs={"Chenel_slug": self.slug})
