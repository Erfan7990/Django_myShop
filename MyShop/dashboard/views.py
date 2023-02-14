from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# import models
from .models import *
from account.models import *
from main.models import *
from order.models import *
from products.models import *


class DashboardHomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'dashboard/index.html')
    
    def post(self, request, *args, **kwargs):
        pass

    
class ProductListView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-uid')
        context={
            'products': products,
        }
        return render(request, 'dashboard/products.html',context)
    
    def post(self, request, *args, **kwargs):
        pass


def add_products(request):
    return render(request, 'dashboard/add-product.html')

def categories(request):
    return render(request, 'dashboard/caterories-list.html')

def add_categories(request):
    return render(request, 'dashboard/add-category.html')