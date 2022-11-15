from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('cart-item/', card_item, name="card_item"),
    path("add-to-card/<uid>/", add_to_cart, name="add_to_card")
]
