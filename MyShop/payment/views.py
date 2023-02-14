from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from MyShop import settings

# models
from .models import *
from account.models import *
from order.models import *
from products.models import *
from payment.models import *
from .forms import BillingAddressForm, PaymentMethodForm

# view
from django.views.generic import TemplateView

# SSL-commerz payment gatway
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt



# Create your views here.
# @login_required(login_url='login')
class Payment_checkout(TemplateView):
    
    def get(self, request, *args, **kwargs):
        try:
            billing_address = BillingAddress.objects.get_or_create(user = request.user or None)
            billing_address = billing_address[0]
            billing_forms = BillingAddressForm(instance= billing_address)

            paymentForm = PaymentMethodForm()
            order_qs =  Orders.objects.filter(user = request.user, ordered=False)
            order_items = order_qs[0].orderItems.all()
            order_total = order_qs[0].get_Total_orders_price()
           

            context = {
                    'Billing_Address_forms': billing_forms,
                    'order_items': order_items,
                    'order_total': order_total,
                    'payment_form': paymentForm
                }

            return render(request, 'payment/checkout.html', context)
        except Exception as e:
            return render(request, 'payment/checkout.html')
        
    def post(self, request, *args, **kwargs):
        billing_address = BillingAddress.objects.get_or_create(user = request.user or None)
        billing_address = billing_address[0]
        billing_forms = BillingAddressForm(instance= billing_address)

        payment_obj = Orders.objects.filter(user=request.user, ordered = False)[0]
        paymentForm = PaymentMethodForm(instance=payment_obj)
        if request.method == 'POST':
            billing_forms = BillingAddressForm(request.POST, instance=billing_address)
            paymentForm = PaymentMethodForm(request.POST, instance=payment_obj)
            if billing_forms.is_valid() and paymentForm.is_valid():
                billing_forms.save()
                pay_method = paymentForm.save()
                


                if pay_method.payment_method == 'Cash on Delivery':
                    order_qs = Orders.objects.filter(user =request.user, ordered = False)
                    order_qs = order_qs[0]
                    order_qs.ordered = True
                    order_qs.orderId = order_qs.uid
                    order_qs.paymentId = pay_method.payment_method
                    order_qs.save()

                    #remove order items from cart
                    cart_item = Cart.objects.filter(user = request.user, purchased = False)
                    for item in cart_item:
                        item.purchased = True
                        item.save()
                    
                if pay_method.payment_method == 'SSLcommerz':
                    storeID = settings.STORE_ID
                    storePASS = settings.STORE_PASS
                    
                    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=storeID, sslc_store_pass=storePASS)
                    
                    status_url = request.build_absolute_uri(reverse('status'))
                    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
                    
                    order_qs = Orders.objects.filter(user=request.user, ordered = False)
                    order_items = order_qs[0].orderItems.all()
                    order_items_count = order_qs[0].orderItems.count()
                    order_total = order_qs[0].get_Total_orders_price()
                    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='clothing', product_name=order_items, num_of_item=order_items_count, shipping_method='Courier', product_profile='None')
                    
                    current_user = request.user
                    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user.email, address1=current_user.profile.address, address2=current_user.profile.address, city=current_user.profile.city, postcode=current_user.profile.zipcode, country=current_user.profile.country, phone=current_user.profile.phone)
                    
                    billing_address = BillingAddress.objects.filter(user = request.user)[0]
                    mypayment.set_shipping_info(shipping_to=billing_address.address, address=billing_address.address, city=billing_address.city, postcode=billing_address.zipcode, country=billing_address.country)
                    response_data = mypayment.init_payment()
                    
                    return redirect(response_data['GatewayPageURL'])

                return redirect('checkout')
        
    # return render(request, 'payment/checkout.html')
@csrf_exempt
def sslc_status(request):
    if request.method == 'POST':
        payment_data = request.POST
        
        print("============")
        print(payment_data)
        print("============")
        
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            
            return HttpResponseRedirect(reverse('sslc_complete', kwargs={'val_id':val_id, 'tran_id':tran_id}))
    return render(request, 'status.html')


def sslc_complete(request, val_id, tran_id):
    order_qs = Orders.objects.filter(user =request.user, ordered = False)
    order_qs = order_qs[0]
    order_qs.ordered = True
    order_qs.orderId = val_id
    order_qs.paymentId = tran_id
    order_qs.save()

    #remove order items from cart
    cart_item = Cart.objects.filter(user = request.user, purchased = False)
    for item in cart_item:
        item.purchased = True
        item.save()
    return redirect('index')
