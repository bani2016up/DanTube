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
            messages.warning(request, 'Smt is wrong.')
            
    return render(request, 'acount/login.html')
        


def logoutUser(request):
    logout(request)
    return redirect('/')

def signupUser(request):
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {'form': form}
    return render(request, 'acount/signup.html', data)    
            
@login_required(login_url='login')            
def acount_page(request):
    user = request.user
    object = CustomUser.objects.filter(username=user)
    data = { 'user': user,
             'object': object}
    return render(request, 'acount/acount.html', data)

def mychenel(request):
  
    
    return render(request, 'acount/Mychenel_page.html')