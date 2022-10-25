from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>/', all_products, name='products'),
    path('product_details/', product_details, name='product-details')
]
