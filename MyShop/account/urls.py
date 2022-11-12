from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name = 'logout'),
    path('registration/', registration, name="registration"),
    path('profile/',user_profile, name='profile')
]