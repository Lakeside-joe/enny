# Generated by Django 4.0.6 on 2022-08-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_shopcart_cart_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='amount',
            field=models.CharField(max_length=50),
        ),
    ]
