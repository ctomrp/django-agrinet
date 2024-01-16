# Generated by Django 4.2.9 on 2024-01-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=12)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=20)),
                ('bussiness_name', models.CharField(max_length=255)),
                ('producer_type', models.CharField(max_length=300)),
                ('birth_date', models.DateField(verbose_name='Fecha de nacimiento')),
            ],
        ),
    ]
