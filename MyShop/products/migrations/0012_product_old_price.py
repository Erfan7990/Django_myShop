# Generated by Django 4.1.6 on 2023-02-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_number_of_stock_product_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(null=True),
        ),
    ]
