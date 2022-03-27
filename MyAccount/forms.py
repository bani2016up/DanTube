
from pyexpat import model
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class signupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'gender', 'interests', 'date_of_birth', 'email', 'password1', 'password2']
        
class chengeUserForm(UserChangeForm):
    class Mete:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2'] 