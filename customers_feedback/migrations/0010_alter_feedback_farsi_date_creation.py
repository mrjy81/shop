# Generated by Django 4.0.5 on 2022-07-13 13:52

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_feedback', '0009_alter_feedback_farsi_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='farsi_date_creation',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 13, 13, 52, 9, 430986, tzinfo=utc), verbose_name='ایجاد شده'),
        ),
    ]
