from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from eshop_orders.models import OrderDetail
from shop_products.models import Products
from sessions_order.cart import Cart
from sessions_order.form import AddToCartForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
import json

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"

amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')

def car_view(request):
    cart = Cart(request)
    form = AddToCartForm()
    if request.user.is_authenticated:
        products = OrderDetail.objects.filter(
            order__owner=request.user,
            order__is_paid=False)
    else:
        products = cart.__iter__()

    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'cart.html', context)


def cart_quantity_delete(request, id):
    cart = Cart(request)
    cart.remove(id)
    return redirect('cart')


def cart_quantity_down(request, id):
    cart = Cart(request)
    cart.qty_down(id)
    return redirect('cart')


def cart_quantity_up(request, id):
    cart = Cart(request)
    cart.qty_up(id)
    return redirect('cart')


@login_required(login_url='/account/login')
def cart_quantity_down_rg(request, id):
    product = get_object_or_404(Products, id=id)
    order = OrderDetail.objects.filter(
        order__owner=request.user,
        order__is_paid=False,
        product=product).first()
    if order.count >= 2:
        qty = order.count
        order.count = qty - 1
        order.price = (qty - 1) * product.price
        order.save()
    return redirect('cart')


def cart_quantity_up_rg(request, id):
    product = get_object_or_404(Products, id=id)
    order = OrderDetail.objects.filter(
        order__owner=request.user,
        order__is_paid=False,
        product=product).first()
    if order.count >= 1:
        qty = order.count
        order.count = qty + 1
        order.price = (qty + 1) * product.price
        order.save()
    return redirect('cart')


def cart_quantity_delete_rg(request, id):
    product = get_object_or_404(Products, id=id)
    order = OrderDetail.objects.filter(
        order__owner=request.user,
        order__is_paid=False,
        product=product).first()
    if order:
        order.delete()
    return redirect('cart')
