# Generated by Django 5.1.4 on 2025-01-08 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comparison',
            old_name='product',
            new_name='products',
        ),
    ]
