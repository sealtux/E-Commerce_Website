from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login/',views.login_views, name = 'log_in'),
    path('forgot/',views.forgot,name = 'forgot'),
    path('shop/',views.shop, name ='shop'),
    path('freeitems/',views.freeitems, name = 'free'),
    path("track/", views.track, name = 'track'),
    path("help/", views.help, name = 'help'),
    path("group/", views.group, name = 'group')
    
]