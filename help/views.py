from django.shortcuts import render

# Create your views here.
def error(request):
    status = 'Auntification error'
    data = {'status': status}
    return render(request, 'help/error.html', data)

def help(request):
    status = 'Help page'
    data = {'status': status}
    return render(request, 'help/main.html', data)

def status(request):
    status = 'Help status'
    data = {'status': status}
    return render(request, 'help/status.html', data)