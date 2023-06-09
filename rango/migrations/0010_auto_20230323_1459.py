# Generated by Django 2.2.28 on 2023-03-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20230321_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('releaseDate', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'shows',
            },
        ),
        migrations.RenameModel(
            old_name='Rating',
            new_name='MovieRating',
        ),
        migrations.CreateModel(
            name='TvRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=2)),
                ('user', models.CharField(default='Anonymous User', max_length=128)),
                ('tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Tv')),
            ],
        ),
    ]
