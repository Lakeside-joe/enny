# Generated by Django 4.0.6 on 2022-08-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_shopcart_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='amount',
            field=models.IntegerField(),
        ),
    ]