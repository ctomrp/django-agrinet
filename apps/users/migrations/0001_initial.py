# Generated by Django 5.0.1 on 2024-01-14 02:40

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('is_userproducer', models.BooleanField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProducerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producerTypeName', models.CharField(max_length=80, verbose_name='Producer Type Name')),
            ],
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='UserProducer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('businessname', models.CharField(max_length=200, verbose_name='Business Name')),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Producer_ProducerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producerType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.producertype', verbose_name='Producer Type')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userproducer', verbose_name='Producer')),
            ],
        ),
    ]
