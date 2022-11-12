from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def login_page(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)

            if not user_obj.exists():
                messages.warning(request, 'Account not Found')
                return HttpResponseRedirect(request.path_info)
            
            user_obj = authenticate(username = username, password = password)

            if user_obj:
                login(request, user_obj)
                username = User.username
                return render(request, 'main/index.html', {'username': username})
            else:
                messages.warning(request, 'Username or password is not correct')
                return HttpResponseRedirect(request.path_info)

        # messages.warning(request, 'Invalid Information')
        return render(request, 'account/login.html')
    except Exception as e:
        print(e)



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
    return redirect('login') 


def user_profile(request):
    # userForm = ProfileForm()
    try:
        if request.method == "POST":
            userForm = ProfileForm(request.POST)
            print(userForm)
            if userForm.is_valid():
                full_name = userForm.cleaned_data['full_name']
                address = userForm.changed_data['address']
                country = userForm.changed_data['country']
                city = userForm.changed_data['city']
                zipcode = userForm.changed_data['zipcode']
                phone = userForm.changed_data['phone']
                save_user_form = Profile(full_name = full_name, address = address, country = country, city = city, zipcode = zipcode, phone = phone)
                save_user_form.save()
                messages.success(request, 'Successfully save user data!!')
                return HttpResponseRedirect(request.path_info)
        else:
            userForm = ProfileForm()
    except Exception as e:
        print(e)
    context = {
        'userForm': userForm
    }
    return render(request, 'account/profile.html', context)