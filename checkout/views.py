from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LX1SNHN3guO7qmCBfFbCmLMVWNwFHd4Psvpzkl5MPHoi9n48DM26r9DnU75RqJ0DYCRl7Thh7augi6bvWJJzq6i00UGATY6R3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
