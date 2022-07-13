# Generated by Django 4.0.5 on 2022-07-12 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_jalali.db.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop_account', '0007_alter_account_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2022, 7, 12, 21, 57, 8, 436654, tzinfo=utc), null=True, verbose_name='تاریخ پیوستن!!!!!!'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]