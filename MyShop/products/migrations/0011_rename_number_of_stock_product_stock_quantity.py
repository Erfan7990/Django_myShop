# Generated by Django 4.1.6 on 2023-02-15 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_number_of_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='number_of_stock',
            new_name='stock_quantity',
        ),
    ]
