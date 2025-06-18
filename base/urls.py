<<<<<<< HEAD
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('Room/',views.room, name = 'room')
=======
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('Room/',views.room, name = 'room')
>>>>>>> 7dc7f0b (Added a new admin feature)
]