from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', Payment_checkout.as_view(), name='checkout'),
    path('sslc/status/', sslc_status, name="status"),
    path('sslc/complete/<val_id>/<tran_id>/', sslc_complete, name="sslc_complete")
]