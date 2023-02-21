from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.

# import models
from .models import *
from account.models import *
from main.models import *
from order.models import *
from products.models import *

# import forms
from .forms import AddProductForm

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


class add_products(TemplateView):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     if request.user.is_superuser == True:
        #         addProduct = AddProductForm()
        #         context = {
        #             'addProductForm' :  addProduct
        #         }
        #         return render(request, 'dashboard/add-product.html', context)
        #     else:
        #         return redirect('admin_home')
        # else:
        #     return redirect('admin_home')
        addProduct = AddProductForm()
        categories = Category.objects.all()
        context = {
            'addProductForm' :  addProduct,
            'categories' : categories
        }

        return render(request, 'dashboard/add-product.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            addProudct = AddProductForm(request.POST)
            if addProudct.is_valid():
                print("+++++++++++++++++======>>>>")
                product = addProudct.save(commit=False)
                slug =  product.product_name.replace(' ','-')
                product.slug = slug
                product.save()
                return redirect('product_list')
            else:
                return redirect('add_product')
        else:
            return redirect('add_product')
    

def categories(request):
    return render(request, 'dashboard/caterories-list.html')

def add_categories(request):
    return render(request, 'dashboard/add-category.html')


def SignIn(request):
    return render(request, 'dashboard/signIn.html')

def forgetPassword(request):
    return render(request, 'dashboard/ForgetPassword.html')

def SignUp(request):
    return render(request, 'dashboard/signUp.html')