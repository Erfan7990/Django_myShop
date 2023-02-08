from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'items', 'quantity','size', 'color', 'purchased', 'price']

    def price(self, obj):
        price = obj.get_total_cart_price()
        return price

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ['user','order_items',  'Order_price', 'paymentId', 'orderId', 'payment_method']
    
    def order_items(self, obj):
        product = obj.orderItems
        return product

    def Order_price(self, obj):
        price = obj.get_Total_orders_price()
        return price

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image']

    def product_name(self, obj):
            product_name = obj.product.product_name
            return product_name
# admin.site.register(Cart)
# admin.site.register(Orders)