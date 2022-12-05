from email import message
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def all_products(request, slug):
    
    try:
        
        product_category = Category.objects.filter(slug = slug)
        if product_category:
            AllProducts = Product.objects.filter(category__slug =slug)
        context = {'AllProducts':AllProducts}
        # print("products", AllProducts)
        return render(request, 'products/all_products.html',context)
            # 

    except Exception as e:
        print(e)
    # return render(request, 'products/all_products.html')
    
def product_details(request, slug, product_slug):
    try:
        if Category.objects.filter(slug = slug):
            if Product.objects.filter(slug = product_slug):
                product = Product.objects.get(slug = product_slug)
                context = {'product': product}
                # print("product", product.product_images.all())
            else:
                messages.warning(request, 'No Product found')
                return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'No Category found')
            return HttpResponseRedirect(request.path_info)

        return render(request, 'products/product_details.html', context)
    except Exception as e:
        print(e)

        
