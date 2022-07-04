from django.shortcuts import render , redirect
from sessions_order.cart import Cart

def add_to_cart_view(request, pr_id):
    cart = Cart(request)
    cart.add_to_cart(pr_id)
    return redirect('product-list')
