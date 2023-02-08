from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>/', all_products, name='products'),
    path('<slug>/<product_slug>/', product_details, name='product_details'),
]
