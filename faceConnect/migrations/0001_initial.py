# Generated by Django 5.0.4 on 2024-04-26 08:48

import django.core.validators
import django.db.models.deletion
import faceConnect.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIndividualImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('index', models.PositiveBigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('mobile_number', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('i_image', models.ImageField(upload_to='individual_face_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), faceConnect.models.validate_file_extension])),
                ('numpy_array', models.BinaryField(blank=True, max_length=16384, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'User Individual Image',
                'verbose_name_plural': 'User Individual Images',
            },
        ),
        migrations.CreateModel(
            name='UserMultipleImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('index', models.PositiveBigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('mobile_number', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('m_image', models.ImageField(upload_to='multiple_face_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), faceConnect.models.validate_file_extension])),
                ('numpy_array', models.BinaryField(blank=True, max_length=16384, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'User Multiple Image',
                'verbose_name_plural': 'User Multiple Images',
            },
        ),
    ]