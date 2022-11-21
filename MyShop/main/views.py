from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from order.models import Orders
from products.models import *
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

# @login_required(login_url='login')
def index(request):
  
    categories = Category.objects.all()
    # order = Orders.objects.get(user = request.user, ordered=False)
    context= {
        'categories': categories,
        }
    return render(request, 'main/index.html', context)
 