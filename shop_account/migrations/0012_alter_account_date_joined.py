# Generated by Django 4.0.5 on 2022-07-13 16:17

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_account', '0011_alter_account_age_alter_account_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2022, 7, 13, 16, 17, 55, 128776, tzinfo=utc), null=True, verbose_name='تاریخ پیوستن!!!!!!'),
        ),
    ]