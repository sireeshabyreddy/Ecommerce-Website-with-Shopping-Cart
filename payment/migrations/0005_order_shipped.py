# Generated by Django 4.2.14 on 2024-08-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_amount_pay_order_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
