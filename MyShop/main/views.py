from django.shortcuts import render
from products.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

@ensure_csrf_cookie
def index(request):
    context= {'categories': Category.objects.all()}
    return render(request, 'main/index.html', context)