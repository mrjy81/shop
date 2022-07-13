from django.db import models
from django.contrib.auth.models import User
from shop_products.models import Products
from django.conf import settings


class Orders(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده', default=False)
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'سبد خزید'
        verbose_name_plural = 'سبد های کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Orders, verbose_name='سبد', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='محصول', on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='قیمت محصول')  # total price
    count = models.PositiveIntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.order.owner.username + ' ' + self.product.title

    class Meta:
        verbose_name = 'جزییات سبد خزید'
        verbose_name_plural = ' جزییات سبد های کاربران'
