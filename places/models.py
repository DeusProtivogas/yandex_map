from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    placeId = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    short_description = models.TextField(blank=True)
    long_description = HTMLField(blank=True)

    coordinates_lon = models.FloatField()
    coordinates_lat = models.FloatField()

    class Meta:
        ordering = ["placeId"]
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return f"{self.title}"


class Photo(models.Model):
    image = models.ImageField(upload_to='')
    position = models.IntegerField(default=1, db_index=True)
    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        related_name="photos",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["position"]

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.position} {self.place.title}"
