from django.shortcuts import render, redirect, get_object_or_404

from eshop_orders.models import OrderDetail
from shop_products.models import Products
from sessions_order.cart import Cart
from sessions_order.form import AddToCartForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
