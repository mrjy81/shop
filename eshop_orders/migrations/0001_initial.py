# Generated by Django 4.0.5 on 2022-07-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت محصول')),
                ('count', models.PositiveIntegerField(verbose_name='تعداد')),
            ],
            options={
                'verbose_name': 'جزییات سبد خزید',
                'verbose_name_plural': ' جزییات سبد های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
            ],
            options={
                'verbose_name': 'سبد خزید',
                'verbose_name_plural': 'سبد های کاربران',
            },
        ),
    ]
