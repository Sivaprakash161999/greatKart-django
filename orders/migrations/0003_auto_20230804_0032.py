# Generated by Django 3.1 on 2023-08-03 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
    ]
