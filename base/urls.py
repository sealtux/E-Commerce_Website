from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login/',views.login_views, name = 'log_in'),
    path('forgot/',views.forgot,name = 'forgot'),
    path('shop/',views.shop, name ='shop')
]