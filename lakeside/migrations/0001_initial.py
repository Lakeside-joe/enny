# Generated by Django 4.1 on 2022-08-09 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_image', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agbada', models.BooleanField(default=False)),
                ('wedding_dress', models.BooleanField(default=False)),
                ('suit', models.BooleanField(default=False)),
                ('gown', models.BooleanField(default=False)),
                ('native', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='food')),
                ('price', models.IntegerField()),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
                ('in_stock', models.BooleanField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lakeside.category')),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
                'db_table': 'Style',
                'managed': True,
            },
        ),
    ]