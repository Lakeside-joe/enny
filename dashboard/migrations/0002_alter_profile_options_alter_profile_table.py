# Generated by Django 4.0.6 on 2022-08-26 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]
