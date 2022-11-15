from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from base.models import BaseModel
# Create your models here.


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    items = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} x {self.items.product_name}"

    def get_total_cart_price(self):
        total_price = self.items.price * self.quantity
        return format(total_price, '0.2f')


class Orders(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    orderItems = models.ManyToManyField(Cart)
    ordered  = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    orderId = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

    def get_Total_orders_price(self):
        total = 0
        for order_item in self.orderItems.all():
            total += float(order_item.get_total_cart_price())
        return total
    