# Generated by Django 4.2.9 on 2024-03-25 12:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeId', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', tinymce.models.HTMLField()),
                ('coordinates_lon', models.FloatField()),
                ('coordinates_lat', models.FloatField()),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='')),
                ('position', models.IntegerField(default=1)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.place', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['position'],
            },
        ),
    ]
