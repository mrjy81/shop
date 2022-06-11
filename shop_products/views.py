from django.shortcuts import render
from django.views.generic import ListView
from .models import Products


class ProductListView(ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        return Products.objects.get_active_products()
