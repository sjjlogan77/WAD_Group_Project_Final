# Generated by Django 2.2.28 on 2023-03-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20230323_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='user',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
