# Generated by Django 4.2.9 on 2024-04-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['placeId'], 'verbose_name': 'Заведение', 'verbose_name_plural': 'Заведения'},
        ),
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]