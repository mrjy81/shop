# Generated by Django 4.0.5 on 2022-07-13 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_account', '0010_account_age_alter_account_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2022, 7, 13, 13, 52, 9, 419192, tzinfo=utc), null=True, verbose_name='تاریخ پیوستن!!!!!!'),
        ),
    ]
