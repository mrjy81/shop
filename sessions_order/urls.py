from django.urls import path
from .views import add_to_cart_view

urlpatterns = [
    path('add-to-cart/<int:pr_id>/', add_to_cart_view, name='add-to-cart'),
]
