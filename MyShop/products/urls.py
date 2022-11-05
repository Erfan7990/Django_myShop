from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>/', all_products, name='products'),
    path('<slug>/<product_slug>/', product_details, name='product_details'),
    path("add-to-card/", add_to_cart, name="add_to_card")
]
