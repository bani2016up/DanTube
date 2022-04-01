from . import views
from django.urls import path

urlpatterns = [
    path('', views.help, name='help'),
    path('status/', views.status, name='help'),
    path('errors/', views.error, name='help'),

]