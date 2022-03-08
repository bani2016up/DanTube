from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']