from django.db import models

# Create your models here.

from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    placeId = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()

    coordinates_lon = models.FloatField()
    coordinates_lat = models.FloatField()


    def __str__(self):
        return f"{self.placeId}"

    class Meta:
        ordering = ["id"]
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Photo(models.Model):
    upload = models.ImageField(upload_to='')
    position = models.IntegerField(default=1)
    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        related_name="photos",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.position} {self.place.title}"

    class Meta:
        ordering = ["position"]

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

