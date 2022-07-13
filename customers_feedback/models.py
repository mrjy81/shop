from django.db import models
from shop_products.models import Products
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Feedback(models.Model):
    BAD = "1"
    NOT_BAD = "2"
    NORMAL = "3"
    GOOD = "4"
    PERFECT = "5"
    RATE_CHOICE = (
        (BAD, _('بد')),
        (NOT_BAD, _('نه چندان بد')),
        (NORMAL, _('معمولی')),
        (GOOD, _('خوب')),
        (PERFECT, _('عالی')),
    )

    about = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='درباره')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    description = models.TextField(verbose_name='توضیحات')
    rate = models.CharField(choices=RATE_CHOICE, max_length=100, verbose_name='رتبه')
    farsi_date_creation = jmodels.jDateTimeField(verbose_name='ایجاد شده',
                                                 default=timezone.now())

    def __str__(self):
        return ' نظر' + self.author.username + " درباره " + self.about.title

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
