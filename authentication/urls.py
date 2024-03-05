from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login_bypass, name='login'),
    path('profile',views.my_profile, name='myprofile'),
    path('profile/admin',views.get_employees, name='adminprofile'),
    path('authorize',views.authorize_change_data, name='auth'),
    
]