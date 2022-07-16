from django.shortcuts import render, redirect
import itertools
from shop_products.models import Products
from siteSetting.models import Settings
from shop_products_category.models import ProductCategory
from django.db import connection
from django.utils import timezone


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# header code behind
def header(request, *args, **kwargs):
    context = {
        'title': 'this is title'
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        "about_us": "این سایت فروشگاهی به وسیله ی django در سایت  ایجاد شده است",

    }
    return render(request, 'shared/Footer.html', context)


# code behind
def home_page(request):
    site_settings = Settings.objects.all()
    category = ProductCategory.objects.all()
    category_with_products = dict()
    today = timezone.localtime(timezone.now())
    latest_products = Products.objects.filter(
        created_at_date__gte=today - timezone.timedelta(hours=2))
    latest_4_4_products = list(my_grouper(4, latest_products))
    for i in category:
        category_with_products[i] = Products.objects.filter(
            active=True, category=i)
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'carousel': site_settings,
        'categories': category,
        'products': category_with_products,
        'latest': latest_4_4_products,
    }
    return render(request, 'home_page.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
