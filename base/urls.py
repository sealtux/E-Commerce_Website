from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login/',views.login, name = 'log_in'),
    path('createRoom/',views.createRoom, name = 'create-room'),
]