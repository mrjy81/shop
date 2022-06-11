from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from shop_products_category.models import ProductCategory


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Products(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=150)
    description = models.TextField(_('توضیحات'))
    price = models.IntegerField(_('قیمت'))
    image = models.ImageField(_('تصویر'), upload_to='products', null=True, blank=True)
    active = models.BooleanField(_('فعال'), default=False)
    category = models.ManyToManyField(ProductCategory, verbose_name=_('دسته بندی'), blank=True)
    objects = ProductManager()

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'productId': self.id})

    def __str__(self):
        return self.title
