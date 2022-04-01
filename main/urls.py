from . import views
from django.urls import path

urlpatterns = [
    path('', views.vidio_page, name='vidio_page'),
    path('search/', views.vidio_search, name='vidio_search'),
    path('new/', views.new_vidio, name='new_vidio'),
    path('<int:pk>/watch/', views.watch_vidio, name='wathc_vido'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('topik=<slug:Chapter_slug>/', views.chapter, name='chapter')

]