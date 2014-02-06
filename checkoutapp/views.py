# -*- coding: utf-8 -*-
import time
from django.http import HttpResponse
from django.shortcuts import render

from checkout import (
    Checkout,
    Contact,
    Payment,
    CheckoutException
)


def onsite(request):
    # Create a Contact object (Optional)
    contact = Contact(
        first_name='Matti',
        last_name='Meikäläinen',
        email='matti.meikalainen@gmail.com',
        address='Esimerkkikatu 123',
        postcode='01234',
        postoffice='Helsinki',
        country='FIN',
        phone='020123456',
        )
    # Create a Payment object
    payment = Payment(
        order_number=str(int(time.time())),
        reference_number='9999999',
        amount='200',
        delivery_date='20140606',
        message='Esimerkkimaksun kuvaus',
        currency='EUR',
        language='FI',
        content='1',
        return_url='https://www.esimerkkikauppa.fi/sv/return',
        cancel_url='https://www.esimerkkikauppa.fi/sv/cancel',
        delayed_url='https://www.esimerkkikauppa.fi/sv/delayed',
        reject_url='https://www.esimerkkikauppa.fi/sv/reject',
        contact=contact
    )
    # Create a Checkout object
    checkout = Checkout()
    # Fetch data for different payment providers for created payment
    data = checkout.get_onsite_button_data(payment)
    # Render with template
    return render(request, "onsite.html", { 'banks': data})

def offsite(request):
    # Create a Contact object (Optional)
    contact = Contact(
        first_name='Matti',
        last_name='Meikäläinen',
        email='matti.meikalainen@gmail.com',
        address='Esimerkkikatu 123',
        postcode='01234',
        postoffice='Helsinki',
        country='FIN',
        phone='020123456',
        )
    # Create a Payment object
    payment = Payment(
        order_number=str(int(time.time())),
        reference_number='9999999',
        amount='200',
        delivery_date='20140606',
        message='Esimerkkimaksun kuvaus',
        currency='EUR',
        language='FI',
        content='1',
        return_url='https://www.esimerkkikauppa.fi/sv/return',
        cancel_url='https://www.esimerkkikauppa.fi/sv/cancel',
        delayed_url='https://www.esimerkkikauppa.fi/sv/delayed',
        reject_url='https://www.esimerkkikauppa.fi/sv/reject',
        contact=contact
    )
    # Create a Checkout object
    checkout = Checkout()
    # Fetch data for different payment providers for created payment
    data = checkout.get_offsite_button_data(payment)
    # Render with template
    return render(request, "offsite.html", { 'formfields': data})

def returnpayment(request):
    # Create a Checkout object
    checkout = Checkout()
    params = request.GET
    if not checkout.validate_payment_return(params['MAC'], params['VERSION'], params['STAMP'], params['REFERENCE'], params['PAYMENT'], params['STATUS'], params['ALGORITHM']):
        return HttpResponse("MAC check failed")
    else:
        if params['STATUS'] in ["2", "5", "6", "8", "9", "10"]:
            return HttpResponse("Payment complete, status code: " + params['STATUS'])
        elif params['STATUS'] == "3":
            return HttpResponse("Payer chose delayed payment, status code: " + params['STATUS'])
        elif params['STATUS'] == "-1":
            return HttpResponse("Payment cancelled, status code: " + params['STATUS'])
        elif params['STATUS'] == "7":
            return HttpResponse("Manual activation requeired, status code: " + params['STATUS'])
        else:
            return HttpResponse("Unknown status code: " + params['STATUS'])

def index(request):
     return render(request, "index.html")

