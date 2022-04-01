from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signupUser, name='signup'),
    path('mychenel/', mychenel, name='mychenel'),
    path("sub/", subs, name="sub"),
    path('', account_page, name='account_page'),

]