from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K2MUSI9ST2KCxBEW8rQuyFvAb7mO1F66C3VEq1fr7yQKcabeI6CLaZPCQ3wxHW7gicHX2jd7g5YSzwXDaktiKJc00ThfGy1FI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
