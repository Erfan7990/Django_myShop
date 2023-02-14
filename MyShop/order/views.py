from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import *
from .models import *
# Create your views here.

@login_required(login_url='login')
def card_item(request):

    try:
        

        carts = Cart.objects.filter(user = request.user, purchased=False)
        order = Orders.objects.filter(user = request.user, ordered=False)
        
        # if Category.objects.filter(slug = slug):
        #     if Product.objects.filter(slug = product_slug):
        #         product = Product.objects.get(slug = product_slug)
        context = {
            'carts': carts,
            'order': order[0].get_Total_orders_price(),
            # 'product': product
        }
    
        return render(request, 'order/add_to_card.html', context)
    except Exception as e:
        return render(request, 'order/add_to_card.html')
        

@login_required(login_url='login')
def add_to_cart(request, uid):
    # items = get_list_or_404(Product, uid = uid)
    items = Product.objects.get(uid=uid)
    cart_item = Cart.objects.get_or_create(items = items, user = request.user, purchased = False)
    order_obj = Orders.objects.filter(user = request.user, ordered = False)
  
    if order_obj.exists():
        order = order_obj[0]
        if order.orderItems.filter(items = items).exists():
            size = request.POST.get('size')
            color = request.POST.get('color')
            quantity = request.POST.get('quantity')
            if quantity:
                cart_item[0].quantity += int(quantity)
            else:
                cart_item[0].quantity += 1
            cart_item[0].size = size
            cart_item[0].color = color
            cart_item[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            size = request.POST.get('size')
            color = request.POST.get('color')
            cart_item[0].size = size
            cart_item[0].color = color
            order.orderItems.add(cart_item[0])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        order = Orders(user = request.user)
        order.save()
        order.orderItems.add(cart_item[0])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # return render(request, 'products/add_to_card.html')

@login_required(login_url='login')
def remove_item(request, uid):
    items = Product.objects.get(uid = uid)
    orders = Orders.objects.filter(user = request.user, ordered = False)

    if orders.exists():
        order = orders[0]
        if order.orderItems.filter(items=items).exists():
            order_item = Cart.objects.filter(items=items, user=request.user, purchased=False)[0]
            order.orderItems.remove(order_item)
            order_item.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def increase_quantity(request, uid):
    items = Product.objects.get(uid = uid)
    print("========")
    print(items.uid)
    print("========")

    orders = Orders.objects.filter(user = request.user, ordered = False)

    if orders.exists():
        order = orders[0]
        if order.orderItems.filter(items = items).exists():
            order_item = Cart.objects.filter(items = items, user = request.user, purchased = False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('card_item')

            else:
                return redirect('card_item')
        else:
            return redirect('card_item')
    else:
        return redirect('card_item')

@login_required(login_url='login')
def decrease_quantity(request, uid):
    items = Product.objects.get(uid = uid)
    orders = Orders.objects.filter(user = request.user, ordered = False)

    if orders.exists():
        order = orders[0]
        if order.orderItems.filter(items = items).exists():
            order_item = Cart.objects.filter(items = items, user = request.user, purchased = False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('card_item')

            else:
                order.orderItems.remove(order_item)
                order_item.delete()
                return redirect('card_item')
        else:
            return redirect('card_item')
    else:
        return redirect('card_item')

