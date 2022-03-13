
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.          

class CustomUser(AbstractUser):
    Chenelname = models.CharField(max_length=32, blank=True)
    datecreated = models.DateField(auto_now_add=True)
    icon = models.ImageField(blank=True)
    backgtound = models.ImageField(blank=True)
    descprion = models.TextField(blank=True)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    subsribetchenels = models.ManyToManyField('CustomUser', blank=True)
    active = models.BooleanField(default=True)
    publick = models.BooleanField(default=True)
    
    
    def get_absolute_url(self):
        return reverse("CustomUser", kwargs={"CustomUser_slug": self.slug})

    