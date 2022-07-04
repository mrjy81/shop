from django.contrib import admin
from eshop_orders.models import OrderDetail, Orders

admin.site.register(Orders)
admin.site.register(OrderDetail)