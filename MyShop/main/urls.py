from django.contrib import admin
from django.urls import path
from .views import index, search_item

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_item, name='search')
]
