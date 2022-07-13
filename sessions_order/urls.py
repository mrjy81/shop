from django.urls import path
from .views import (
    add_to_cart_view,
    add_to_cart_view_rg
)

urlpatterns = [
    path('add-to-cart/<str:pr_id>/', add_to_cart_view, name='add-to-cart'),
    path('add-to-cart-rg/<str:id>/', add_to_cart_view_rg, name='add-to-cart-rg'),  # registered

]
