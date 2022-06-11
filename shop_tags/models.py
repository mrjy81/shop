from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _
from shop_products.models import Products

class Tag(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=150)
    slug = models.SlugField(verbose_name=_('عنوان در url'),null=True , blank=True)
    timestamp = models.DateTimeField(verbose_name=_('برچسب زمان'), auto_now_add=True)
    active = models.BooleanField(verbose_name=_('فعال'), default=False)
    products = models.ManyToManyField(Products, blank=True)

    class Meta:
        verbose_name = _('برچسب / تگ')
        verbose_name_plural = _('برچسب ها')

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
