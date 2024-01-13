# Generated by Django 4.2.9 on 2024-01-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('razon_social', models.CharField(max_length=255)),
                ('tipo_productor', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField(verbose_name='Birthdate')),
            ],
        ),
    ]
