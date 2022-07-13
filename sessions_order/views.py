from django.shortcuts import render, redirect, get_object_or_404
from sessions_order.cart import Cart
from .form import AddToCartForm
from django.urls import reverse
from shop_products.models import Products
from eshop_orders.models import Orders, OrderDetail
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def add_to_cart_view(request, pr_id):
    form = AddToCartForm()
    product = Products.objects.get(id=pr_id)
    if request.method == "POST":
        form = AddToCartForm(request.POST or None)
    if form.is_valid():
        qty = form.cleaned_data['count']
        cart = Cart(request)
        cart.add_to_cart(pr_id, qty, product.price)
    return redirect('product-detail', productId=pr_id)


@login_required(login_url='/account/login')
def add_to_cart_view_rg(request, id):
    form = AddToCartForm()
    if request.method == "POST":
        form = AddToCartForm(request.POST or None)
    if form.is_valid():
        qty = form.cleaned_data['count']
        order = Orders.objects.filter(owner=request.user, is_paid=False).first()
        product = get_object_or_404(Products, id=id)

        if not order:
            order = Orders.objects.create(owner=request.user, is_paid=False)
        try:
            order_detail = OrderDetail.objects.get(
                order=order,
                product=product,
            )
        except ObjectDoesNotExist:
            OrderDetail.objects.create(
                order=order,
                product=product,
                count=qty,
                price=qty * product.price,
            )
        else:
            print('obj found')
            if order_detail.count != qty:
                order_detail.count = qty
                order_detail.price = qty * product.price
                order_detail.save()

    return redirect('product-detail', productId=id)
