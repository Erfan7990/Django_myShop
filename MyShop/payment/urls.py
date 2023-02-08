from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', Payment_checkout.as_view(), name='checkout'),
]