from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('cart-item/', card_item, name="card_item"),
    path("add-to-card/<uid>/", add_to_cart, name="add_to_card"),
    path('remove-card/<uid>', remove_item, name='remove_card')
]
