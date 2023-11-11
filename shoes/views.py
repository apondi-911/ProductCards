from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient

from shoes.forms import PaymentForm
from shoes.models import Shoes


def home(request):
    shoes = Shoes.objects.all()
    return render(request, 'webpage/home.html', {'shoes': shoes})


def cart(request):
    return render(request, 'webpage/cart.html')


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            client = MpesaClient()
            phone_number = '0701582114'
            amount = 1
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

            if hasattr(response, 'ResponseCode') and response.ResponseCode == '0':
                # Payment was successful, add a success message
                messages.success(request, 'Payment successful.')
            else:
                messages.error(request, 'Payment failed. Please try again.')

            return HttpResponse(response)

        return HttpResponse("Payment initiated successfully.")
    else:
        form = PaymentForm()

    return render(request, 'webpage/payment.html', {'form': form})


def add_to_cart(request, shoe_id):
    cart = request.session.get('cart', {})
    cart[shoe_id] = cart.get(shoe_id, 0) + 1
    request.session['cart'] = cart
    return redirect('home-url')


def view_cart(request):
    cart = request.session.get('cart', {})

    # Retrieve the shoe objects for the items in the cart
    shoes_in_cart = []
    for shoe_id, item in cart.items():
        shoe = Shoes.objects.get(id=shoe_id)
        shoes_in_cart.append({'shoe': shoe, 'quantity': item['quantity']})

    return render(request, 'webpage/cart.html', {'shoes_in_cart': shoes_in_cart})
