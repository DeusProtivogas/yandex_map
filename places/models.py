from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    placeId = models.BigAutoField(
        primary_key=True,
        verbose_name="Уникальный ключ заведения",
    )
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название заведения",
    )
    short_description = models.TextField(
        blank=True,
        verbose_name="Краткое описание",
    )
    long_description = HTMLField(
        blank=True,
        verbose_name="Полное описание",
    )

    coordinates_lon = models.FloatField(
        verbose_name="Долгота",
    )
    coordinates_lat = models.FloatField(
        verbose_name="Широта",
    )

    class Meta:
        ordering = ["placeId"]
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return f"{self.title}"


class Photo(models.Model):
    image = models.ImageField(
        upload_to='',
        verbose_name="Фотография",
    )
    position = models.IntegerField(
        default=1,
        db_index=True,
        verbose_name="Позиция",
    )
    place = models.ForeignKey(
        Place,
        verbose_name="Заведение",
        related_name="photos",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["position"]

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.position} {self.place.title}"
