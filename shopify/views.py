from django.shortcuts import render, redirect
from siteSetting.models import Settings


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
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'carousel': site_settings,
    }
    return render(request, 'home_page.html', context)
