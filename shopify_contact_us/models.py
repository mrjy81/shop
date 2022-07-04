from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='نام', max_length=255)
    email = models.EmailField(verbose_name='ایمیل',max_length=155)
    subject = models.CharField(verbose_name='موضوع',max_length=100)
    message = models.TextField(verbose_name='پیغام')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'اطلاعات تماس با ما'

    def __str__(self):
        return self.name


