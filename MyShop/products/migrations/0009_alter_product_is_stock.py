# Generated by Django 4.1.6 on 2023-02-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_is_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_stock',
            field=models.BooleanField(default=True),
        ),
    ]
