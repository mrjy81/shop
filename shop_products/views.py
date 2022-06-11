from django.shortcuts import render
from django.views.generic import ListView
from .models import Products
from django.http import Http404
from django.db.models import Q


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
    product_id = kwargs.get('productId')
    qs = Products.objects.get_by_id(product_id)
    context = dict()
    if qs is None or not qs.active:
        raise Http404

    context['product'] = qs

    return render(request, 'product_detail.html', context)
