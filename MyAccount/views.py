from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import signupForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Password or username is wrong.')
            
    return render(request, 'account/login.html')
        


def logoutUser(request):
    logout(request)
    return redirect('/')

def signupUser(request):
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            form.save_m2m()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
            
            
    data = {'form': form}
    return render(request, 'account/signup.html', data)    
            
@login_required(login_url='login')            
def account_page(request):
    user = request.user
    object = CustomUser.objects.filter(username=user)
    data = { 'user': user,
             'object': object}
    return render(request, 'account/account.html', data)

def mychenel(request):
    user = request.user
    
    data = {
        'user' : user
    }
    
    return render(request, 'account/Mychenel_page.html', data)

def subs(request):
    pass