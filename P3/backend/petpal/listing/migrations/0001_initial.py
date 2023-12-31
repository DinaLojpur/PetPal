# Generated by Django 5.0 on 2023-12-16 01:33

import django.core.files.storage
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE')], max_length=10)),
                ('breed', models.CharField(choices=[('bunny', 'BUNNY'), ('cat', 'CAT'), ('dog', 'DOG')], max_length=10)),
                ('neutered', models.BooleanField(default=False)),
                ('vaccinated', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=250, null=True)),
                ('on_hold', models.BooleanField(default=False)),
                ('medical_records', models.FileField(null=True, upload_to='records/')),
                ('picture1', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media'), upload_to='photos/')),
                ('picture2', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media'), upload_to='photos/')),
                ('picture3', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media'), upload_to='photos/')),
                ('picture4', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media'), upload_to='photos/')),
                ('shelter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('notes', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('denied', 'Denied'), ('withdrawn', 'Withdrawn')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('seeker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='listing.listing')),
            ],
        ),
    ]
