# Generated by Django 4.1.1 on 2022-11-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orders_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]