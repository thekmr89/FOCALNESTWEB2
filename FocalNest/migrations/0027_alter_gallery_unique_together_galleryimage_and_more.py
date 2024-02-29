# Generated by Django 4.2.7 on 2023-11-19 04:53

import FocalNest.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0026_gallery_images'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gallery',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=FocalNest.models.gallery_image_path)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FocalNest.gallery')),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
    ]