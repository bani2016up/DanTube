from datetime import datetime
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.          



class CustomUser(AbstractUser):
    GENDER = (
        ('Man', 'male'),
        ('Woman', 'female'),
        ('Other', 'Other'),
        )
    INTERESTS = (
        ('PCGames', 'PC Games'),
        ('IT', 'IT'),
        ('Study', 'Study'),
        ('Musik', 'Musik'),
        ('Sports', 'Sports'),
        ('DIY', 'DIY'),
        ('Decor', 'Decor'),
        ('Feashion', 'Feashion'),
        ('Other', 'Other'),
        
    )
    
    Chenelname = models.CharField(max_length=32, blank=True)
    datecreated = models.DateField(auto_now_add=True)
    icon = models.ImageField(blank=True)
    backgtound = models.ImageField(blank=True)
    descprion = models.TextField(blank=True)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    subsribetchenels = models.ManyToManyField('CustomUser', blank=True)
    active = models.BooleanField(default=True)
    publick = models.BooleanField(default=True)
    
    gender = models.CharField(max_length=8, choices = GENDER)
    interests = models.ManyToManyField('main.Chapter')
    date_of_birth = models.DateField(null=True)
    
    
    def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25  )

    
    
    def get_absolute_url(self):
        return reverse("CustomUser", kwargs={"CustomUser_slug": self.slug})

    