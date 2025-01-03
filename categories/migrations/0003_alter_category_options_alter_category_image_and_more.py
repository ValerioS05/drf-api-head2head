# Generated by Django 5.1.4 on 2024-12-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default_h2h', null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
