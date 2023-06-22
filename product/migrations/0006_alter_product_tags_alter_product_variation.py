# Generated by Django 4.2.1 on 2023-05-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.producttag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='variation',
            field=models.ManyToManyField(blank=True, to='product.productvariation'),
        ),
    ]