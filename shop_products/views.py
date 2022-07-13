from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from sessions_order.cart import Cart
from .models import Products
from django.http import Http404
from django.db.models import Q
from shop_tags.models import Tag
from shop_products_category.models import ProductCategory
from sessions_order.form import AddToCartForm
from customers_feedback.forms import FeedbackForm
from customers_feedback.models import Feedback
from customers_feedback.models import Feedback


class ProductListView(ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            qs = Products.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)).distinct()
            return qs
        else:
            return Products.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    cart = Cart(request)
    product_id = kwargs.get('productId')
    qs = Products.objects.get_by_id(product_id)
    form_feedback = FeedbackForm()
    context = dict()
    feedbacks = Feedback.objects.filter(about=product_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            form_feedback = FeedbackForm(request.POST or None)
            if form_feedback.is_valid():
                saved_form = form_feedback.save(commit=False)
                saved_form.author = request.user
                saved_form.about = get_object_or_404(Products, id=product_id)
                saved_form.save()
            else:
                print(form_feedback.cleaned_data)
                print(form_feedback.errors)
        else:
            return redirect('login')

    if qs is None or not qs.active:
        raise Http404
    qty = 1
    a = cart.is_exist(product_id)
    if a:
        qty = a['qty']

    recommended_products = Products.objects.filter(
        Q(tag__products=qs)
    )
    context['product'] = qs
    context['recommended_products'] = recommended_products
    context['qty'] = qty
    context['form_feedback'] = form_feedback
    context['feedbacks'] = feedbacks

    return render(request, 'product_detail.html', context)
