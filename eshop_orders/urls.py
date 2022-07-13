from django.urls import path
from .views import (
    car_view,
    cart_quantity_delete,
    cart_quantity_down,
    cart_quantity_up,
    cart_quantity_down_rg,
    cart_quantity_up_rg,
    cart_quantity_delete_rg,

)

urlpatterns = [
    path('cart', car_view, name='cart'),
    path('cart_quantity_delete/<str:id>', cart_quantity_delete, name='cart_quantity_delete'),
    path('cart_quantity_down/<str:id>', cart_quantity_down, name='cart_quantity_down'),
    path('cart_quantity_up/<str:id>', cart_quantity_up, name='cart_quantity_up'),

    path('cart_quantity_down_rg/<str:id>', cart_quantity_down_rg, name='cart_quantity_down_rg'),
    path('cart_quantity_up_rg/<uuid:id>', cart_quantity_up_rg, name='cart_quantity_up_rg'),
    path('cart_quantity_delete_rg/<uuid:id>', cart_quantity_delete_rg, name='cart_quantity_delete_rg'),
]
