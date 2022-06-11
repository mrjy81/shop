from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)


class Products(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=150)
    description = models.TextField(_('توضیحات'))
    price = models.IntegerField(_('قیمت'))
    image = models.ImageField(_('تصویر'), upload_to='products', null=True, blank=True)
    active = models.BooleanField(_('فعال'), default=False)
    objects = ProductManager()

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')

    def __str__(self):
        return self.title
