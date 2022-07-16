from django.contrib import admin
from eshop_orders.models import OrderDetail, Orders, FinishedOrder


class FinishedOrderAdmin(admin.ModelAdmin):
    change_list_template = 'admin/finishedorder/change_list.html'


class OrdersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('قسمت اول', {
            'fields': ('owner', 'is_paid'),
            'description': 'اطلاعات قسمت اول',
        }),
        ('زمان', {
            'fields': ('payment_date',),
            'description': 'اطلاعات زمان پرداخت ',
            'classes': ['collapse'],

        }),
    ]


admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderDetail)
admin.site.register(FinishedOrder, FinishedOrderAdmin)
