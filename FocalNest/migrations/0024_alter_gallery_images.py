# Generated by Django 4.2.7 on 2023-11-19 04:33

import FocalNest.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0023_gallery_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ImageField(upload_to=FocalNest.models.gallery_image_path),
        ),
    ]