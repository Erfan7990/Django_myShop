from django import template
from order.models import Orders, Cart

from django import template

register = template.Library()

@register.filter
def cart_counter(user):
    order = Orders.objects.filter(user = user, ordered=False)
    if order.exists():
        return order[0].orderItems.count()
    else:
        return 0
