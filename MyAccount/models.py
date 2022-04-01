from datetime import datetime
from email.policy import default
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
    icon = models.ImageField(blank=True, default='users_defult/05e93d6ba2e8e9076a51b5eece3a12f1_400x400.png')
    backgtound = models.ImageField(blank=True, default='users_defult/depositphotos_56588069-stock-photo-earth-view-from-space-at.jpg')
    descprion = models.TextField(blank=True)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    subsribetchenels = models.ManyToManyField('CustomUser', blank=True)
    active = models.BooleanField(default=True)
    publick = models.BooleanField(default=True)
    
    gender = models.CharField(max_length=8, choices = GENDER)
    interests = models.ManyToManyField('main.Chapter')
    date_of_birth = models.DateField(null=True)
    
    
    def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)

    
    
    def get_absolute_url(self):
        return reverse("CustomUser", kwargs={"CustomUser_slug": self.slug})

    