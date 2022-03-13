from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signupUser, name='signup'),
    path('mychenel/', mychenel, name='mychenel'),
    path('', acount_page, name='acount_page'),

]