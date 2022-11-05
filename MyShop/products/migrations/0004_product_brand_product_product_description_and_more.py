# Generated by Django 4.1.1 on 2022-10-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='product_details',
        ),
    ]