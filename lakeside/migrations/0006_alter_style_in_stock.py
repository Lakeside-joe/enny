# Generated by Django 4.1 on 2022-08-18 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakeside', '0005_alter_style_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='in_stock',
            field=models.BooleanField(),
        ),
    ]
