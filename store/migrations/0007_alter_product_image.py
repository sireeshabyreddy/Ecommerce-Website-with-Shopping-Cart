# Generated by Django 4.2.13 on 2024-12-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_email_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='media/uploads/product/Php_programming.jpeg', null=True, upload_to='uploads/product/'),
        ),
    ]
