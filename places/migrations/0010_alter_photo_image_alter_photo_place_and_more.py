# Generated by Django 4.2.9 on 2024-04-07 16:04

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_options_remove_place_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.place', verbose_name='Заведение'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='position',
            field=models.IntegerField(db_index=True, default=1, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lon',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Уникальный ключ заведения'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название заведения'),
        ),
    ]
