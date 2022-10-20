from django.shortcuts import render

# Create your views here.

def all_products(request):
    return render(request, 'products/all_products.html')

def product_details(request):
    return render(request, 'products/product_details.html')
