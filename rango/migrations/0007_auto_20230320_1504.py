# Generated by Django 2.1.5 on 2023-03-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20230320_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
    ]