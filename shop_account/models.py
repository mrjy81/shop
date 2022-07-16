from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True ,editable=False)
    date_joined = jmodels.jDateTimeField(_('تاریخ پیوستن!!!!!!'), default=timezone.now(), blank=True, null=True)
    last_login = jmodels.jDateTimeField(_("آخرین بازدید !!!"), blank=True, null=True)
    age = models.PositiveIntegerField(null=True , blank=True)

    def save(self, *args, **kwargs):
        self.last_login = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
