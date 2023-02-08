from django.contrib import admin
from .models import *
# Register your models here

@admin.register(BillingAddress)
class AdminBillingAddress(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country', 'address', 'city', 'zipcode', 'phone_number']
