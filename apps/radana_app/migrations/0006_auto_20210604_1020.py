# Generated by Django 2.2.4 on 2021-06-04 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radana_app', '0005_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='items',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items_order',
        ),
    ]
