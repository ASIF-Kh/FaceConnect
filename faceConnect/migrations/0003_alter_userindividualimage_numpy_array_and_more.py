# Generated by Django 5.0.4 on 2024-04-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceConnect', '0002_remove_userindividualimage_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userindividualimage',
            name='numpy_array',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermultipleimage',
            name='numpy_array',
            field=models.TextField(blank=True, null=True),
        ),
    ]