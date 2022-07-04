from django.db import models


class Settings(models.Model):
    carousel_image = models.ImageField(upload_to='siteSettings/')
    carousel_title = models.CharField(max_length=155)
    carousel_title2 = models.CharField(max_length=155)
    carousel_text = models.TextField()

    def __str__(self):
        return self.carousel_title

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'
