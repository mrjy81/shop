# Generated by Django 4.0.5 on 2022-07-12 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='farsi_date_creation',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 12, 12, 7, 40, 591948, tzinfo=utc), verbose_name='ایجاد شده'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.CharField(choices=[(1, 'بد'), (2, 'نه چندان بد'), (3, 'معمولی'), (4, 'خوب'), (5, 'عالی')], max_length=100, verbose_name='رتبه'),
        ),
    ]
