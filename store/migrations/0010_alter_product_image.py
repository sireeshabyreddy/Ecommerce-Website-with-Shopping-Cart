# Generated by Django 4.2.13 on 2024-12-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='uploads/product/Php_programming.jpeg', null=True, upload_to='uploads/product/'),
        ),
    ]
