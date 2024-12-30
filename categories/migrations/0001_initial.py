# Generated by Django 5.1.4 on 2024-12-30 14:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, default='../default_h2h', max_length=255, null=True, verbose_name='image')),
            ],
        ),
    ]
