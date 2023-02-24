from django.shortcuts import render, redirect
from django.views.generic import TemplateView , DeleteView
# Create your views here.

# import models
from .models import *
from account.models import *
from main.models import *
from order.models import *
from products.models import *

# import forms
from .forms import AddProductForm , AddCategoryForm

class DashboardHomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'dashboard/index.html')
    
    def post(self, request, *args, **kwargs):
        pass

"""
    Working with Product Items
"""
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
                # product = addProudct.save(commit=False)
                # slug =  product.product_name.replace(' ','-')
                # product.slug = slug
                # product.save()
                addProudct.save()
                return redirect('product_list')
            else:
                return redirect('add_product')
        else:
            return redirect('add_product')
#
## Edit Product Information
#
class EditProduct(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug = slug)
        EditProductForm = AddProductForm(instance=product)
        context = {
            'EditProductForm': EditProductForm
        }
        return render(request, 'dashboard/add-product.html', context)
        
    def post(self, request, slug, *args, **kwargs):
        if request.method == 'POST':
            product = Product.objects.get(slug = slug)
            EditProudct = AddProductForm(request.POST, instance=product)
            if EditProudct.is_valid():
                print("+++++++++++++++++======>>>>")
                # product = addProudct.save(commit=False)
                # slug =  product.product_name.replace(' ','-')
                # product.slug = slug
                # product.save()
                EditProudct.save()
                return redirect('product_list')
            else:
                return redirect('add_product')
        else:
            return redirect('add_product')

class DeleteProduct(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug = slug)
        product.delete()
        return redirect('product_list')


"""
    Working with Categories
"""

class categories(TemplateView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'dashboard/caterories-list.html', context)
    
    
    def post(self, request, *args, **kwargs):
        pass

class add_categories(TemplateView):
    def get(self, request, *args, **kwargs):
        add_category_form = AddCategoryForm()
        context = {
            'add_category_form': add_category_form
        }
        return render(request, 'dashboard/add-category.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            add_category_form = AddCategoryForm(request.POST, request.FILES)
            if add_category_form.is_valid():
                add_category_form.save()
                
                return redirect('categories_list')
            else:
                return redirect('edit_category')
        else:
            return redirect('edit_category')

class edit_category(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        categories = Category.objects.get(slug = slug)
        add_category_form = AddCategoryForm(instance=categories)
        context = {
            'add_category_form':add_category_form
        }
        return render(request, 'dashboard/add-category.html', context)
    
    
    def post(self, request, slug, *args, **kwargs):
        if request.method == 'POST':
            categories = Category.objects.get(slug = slug)
            add_category_form = AddCategoryForm(request.POST, request.FILES, instance=categories)
            if add_category_form.is_valid():
                add_category_form.save()
                
                return redirect('categories_list')
            else:
                return redirect('add_categories')
        else:
            return redirect('add_categories')

class DeleteCategory(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        category = Category.objects.get(slug = slug)
        category.delete()
        return redirect('categories_list')

def SignIn(request):
    return render(request, 'dashboard/signIn.html')

def forgetPassword(request):
    return render(request, 'dashboard/ForgetPassword.html')

def SignUp(request):
    return render(request, 'dashboard/signUp.html')