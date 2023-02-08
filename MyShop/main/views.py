from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from order.models import *
from products.models import *
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

# @login_required(login_url='login')
def index(request):
  
    categories = Category.objects.all()
    banners = Banner.objects.filter(is_active = True).order_by('uid')
    # order = Orders.objects.get(user = request.user, ordered=False)
    context= {
        'categories': categories,
        'banners' : banners
        }
    return render(request, 'main/index.html', context)
 


def search_item(request):
    if request.method == 'GET':
        item = request.GET.get('query')
        products = Product.objects.filter(product_name__icontains = item)

        context = {
            'products': products
        }
    return render(request, 'base/search.html', context)