# Generated by Django 5.1.7 on 2025-03-27 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, verbose_name='Полное название Категорий')),
            ],
            options={
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='AdminCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('discount_price', models.IntegerField(default=0)),
                ('is_sold', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('full_price', models.IntegerField()),
                ('date', models.DateField()),
                ('is_take_away', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='admin_car/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('discount', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Marka.admincategory')),
            ],
        ),
    ]
