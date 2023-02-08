from django import forms
from .models import *
from order.models import *

class BillingAddressForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Last Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Address'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Country'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'City'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'ZipCode'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Mobile Number'}))
    class Meta:
        model = BillingAddress
        fields = ['first_name', 'last_name', 'country', 'address', 'city', 'zipcode', 'phone_number']

class PaymentMethodForm(forms.ModelForm):
    # payment_method = forms.CharField(widget=forms.RadioSelect())
    class Meta:
        model = Orders
        fields = ['payment_method']

        