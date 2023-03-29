from django.http import HttpResponseRedirect ,HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from .models import Profile
from .forms import ProfileForm
from payment.forms import BillingAddressForm

#models
from products.models import *
from order.models import *
from account.models import *
from payment.models import *

#default template
from django.views.generic import TemplateView

# Create your views here.
def login_page(request):
        # if request.user.is_authenticated:
        #     return redirect('index')
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not Found')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = username, password = password)

        if user_obj is not None:
            login(request, user_obj)
            # username = User.username
            return redirect('index')
        else:
            messages.warning(request, 'Username or password is not correct')
            return HttpResponseRedirect(request.path_info)
    
        # messages.warning(request, 'Invalid Information')
        # context = { 'username': username}
    else:
        if request.user.is_superuser == True:
            messages.warning(request, 'Admin user can not login')
        
    return render(request, 'account/login.html')



def registration(request):
    forms = SignUpForm()
    try:
        if request.method == "POST":
            forms = SignUpForm(request.POST)
            if forms.is_valid():
                forms.save()
                # userForm = forms.save()
                # profile = Profile.objects.create(user = userForm)
                # profile.save()
                # userForm.save()
                messages.success(request, 'Account Created Successfully!!')
                return HttpResponseRedirect(request.path_info)
        else:
            forms = SignUpForm()
    except Exception as e:
        print(e)
    context = {'forms': forms}
    return render(request, 'account/registration.html', context)

def logout_page(request):
    logout(request)
    return render(request, 'account/login.html')


# def user_profile(request):
#     userForm = ProfileForm()
#     try:
#         # print(profile_obj)
#         if request.method == "POST":
#             profile_obj = Profile.objects.get(user = request.user)
#             userForm = ProfileForm(request.POST, instance = profile_obj)
#             if userForm.is_valid():
#                 userForm.save()
#                 messages.success(request, 'Successfully save user data!!')
#                 return HttpResponseRedirect(request.path_info)
#         else:
#             profile_obj = Profile.objects.get(user = request.user)

#     except Exception as e:
#         print(e)
#     context = {
#         'userForm': userForm,
#         'profile': profile_obj
#     }
#     return render(request, 'account/profile.html', context)

# @login_required(login_url='login')
class user_profile(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            orders = Orders.objects.filter(user= request.user, ordered=True)
            billingAddress = BillingAddress.objects.get(user=request.user)
            Billing_Address_forms = BillingAddressForm(instance=billingAddress)
            context={
                'orders' : orders,
                'billingAddress': billingAddress,
                'Billing_Address_forms': Billing_Address_forms
            }
            return render(request, 'account/profile.html', context)
        else:
            return redirect('login')
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            billingAddress = BillingAddress.objects.get(user=request.user)
            Billing_Address_forms = BillingAddressForm(request.POST, instance=billingAddress)
            if Billing_Address_forms.is_valid():
                Billing_Address_forms.save()
           
                return redirect('profile')