from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=150)
    name = models.CharField(verbose_name=_('نام'), max_length=150)

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها ')
