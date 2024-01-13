# Generated by Django 4.2.9 on 2024-01-13 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Product name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('stock', models.IntegerField(verbose_name='Products in stock')),
                ('description', models.TextField(verbose_name='Description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Category')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productname', verbose_name='Name')),
            ],
        ),
    ]
