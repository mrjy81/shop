from django.urls import path, include
from .views import ProductListView, product_detail

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<productId>', product_detail, name='product-detail'),
]
