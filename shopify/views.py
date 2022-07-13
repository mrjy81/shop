from django.shortcuts import render, redirect

from shop_products.models import Products
from siteSetting.models import Settings
from shop_products_category.models import ProductCategory


# header code behind
def header(request, *args, **kwargs):
    context = {
        'title': 'this is title'
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        "about_us": "این سایت فروشگاهی به وسیله ی django در سایت Topelarn ایجاد شده است",

    }
    return render(request, 'shared/Footer.html', context)


# code behind
def home_page(request):
    site_settings = Settings.objects.all()
    category = ProductCategory.objects.all()
    category_with_products = dict()
    for i in category:
        category_with_products[i] = Products.objects.filter(active=True, category=i)
    print(category_with_products)
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'carousel': site_settings,
        'categories': category,
        'products': category_with_products,
    }
    return render(request, 'home_page.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
