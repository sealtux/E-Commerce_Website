from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('Room/',views.room, name = 'room'),
    path('createRoom/',views.createRoom, name = 'create-room'),
]