from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from products.models import Product
from .models import *
# Create your views here.

def card_item(request):
    carts = Cart.objects.filter(user = request.user, purchased=False)
    order = Orders.objects.filter(user = request.user, ordered=False)
  
    context = {
        'carts': carts,
        'order': order[0].get_Total_orders_price()
    }
   
    return render(request, 'order/add_to_card.html', context)

def add_to_cart(request, uid):
    # items = get_list_or_404(Product, uid = uid)
    items = Product.objects.get(uid=uid)
    cart_item = Cart.objects.get_or_create(items = items, user = request.user, purchased = False)
    order_obj = Orders.objects.filter(user = request.user, ordered = False)
  
    if order_obj.exists():
        order = order_obj[0]
        if order.orderItems.filter(items = items).exists():
            cart_item[0].quantity += 1
            cart_item[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            order.orderItems.add(cart_item[0])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        order = Orders(user = request.user)
        order.save()
        order.orderItems.add(cart_item[0])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # return render(request, 'products/add_to_card.html')
