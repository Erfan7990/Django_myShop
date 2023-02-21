from django import forms
from django.forms.models import ModelForm

# Import Models
from products.models import *
from account.models import *



class AddProductForm(ModelForm):
    product_name =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box'}))
    
    category =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-select input-box'}))
    price =  forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-box'}))
    old_price =  forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-box'}))
    brand =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box'}))
    # is_stock = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Full Name'}))
    stock_quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-box'}))
    product_description =  forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control input-box'}))
    
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ('slug',)