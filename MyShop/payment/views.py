from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# models
from .models import *
from order.models import *
from .forms import BillingAddressForm, PaymentMethodForm

# view
from django.views.generic import TemplateView




# Create your views here.

class Payment_checkout(TemplateView):
    def get(self, request, *args, **kwargs):
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
                    


                    return redirect('card_item')
        
    # return render(request, 'payment/checkout.html')
