# Generated by Django 2.2.28 on 2023-03-24 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0015_auto_20230324_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avgRating',
            field=models.FloatField(default=-1),
        ),
    ]
