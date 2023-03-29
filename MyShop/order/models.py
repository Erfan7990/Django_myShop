from django.db import models
from django.contrib.auth.models import User
from products.models import *
from base.models import BaseModel

from decimal import Decimal
# Create your models here.


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    items = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(null=True, blank=True, max_length=50)
    color = models.CharField(null=True, blank=True, max_length=50)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} x {self.items.product_name}"

    def get_total_cart_price(self):
        total_price = self.items.price * self.quantity
        return format(total_price, '0.2f')

    def get_variation_price(self):
        sizes = variationValue.objects.filter(variation = 'size', product = self.items)
        colors = variationValue.objects.filter(variation = 'color', product = self.items)
        
        for size in sizes:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        color_price = color.price
                if size.name == self.size:
                    price = size.price + color_price
                    return format(price, '0.2f')
            else:
                if size.name == self.size:
                    price = size.price
                    return format(price, '0.2f')
    
    def get_variation_base_price(self):
        variation_price = self.get_variation_price()
        price = float(self.items.price) + float(variation_price)
        return format(price, '0.2f')


    def total_price(self):
        variation_price = self.get_variation_base_price()
        price = float(self.quantity) * float(variation_price)
        return format(price, '0.2f')

    
PAYMENT_METHOD = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('PayPal', 'PayPal'),
    ('SSLcommerz', 'SSLcommerz'),
)
class Orders(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    orderItems = models.ManyToManyField(Cart)
    ordered  = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    orderId = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length= 30, choices=PAYMENT_METHOD, default='Cash on Delivery')

    def __str__(self):
        return self.user.username

    def get_Total_orders_price(self):
        total = 0
        for order_item in self.orderItems.all():
            total += float(order_item.total_price())
        return format(total, '0.2f')
    
    def total_amount(self):
        total = Decimal(0)
        total += Decimal(self.get_Total_orders_price())
        return total
        


class Banner(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    image = models.ImageField(upload_to="banner")
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.product_name