from django.db import models
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from main.models import Chenele
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    date = models.DateField(auto_now_add=True)
    sub_chenls = models.ManyToManyField(Chenele, blank=True)

    def __str__(self):
        return self.user