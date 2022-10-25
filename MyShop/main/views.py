from django.shortcuts import render
from products.models import *
# Create your views here.

def index(request):
    context= {'categories': Category.objects.all()}
    return render(request, 'main/index.html', context)