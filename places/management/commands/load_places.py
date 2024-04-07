import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Photo


class Command(BaseCommand):
    help = "Add more locations to the database"

    def add_arguments(self, parser):
        parser.add_argument("json_address", nargs="+", type=str)

    def handle(self, *args, **options):
        try:
            for address in options["json_address"]:
                response = requests.get(address,)

                new_place, created = Place.objects.get_or_create(
                    title=response.json()["title"],
                    short_description=response.json()["description_short"],
                    long_description=response.json()["description_long"],
                    coordinates_lon=response.json()["coordinates"]["lng"],
                    coordinates_lat=response.json()["coordinates"]["lat"],
                )
                if created:
                    new_place.placeId = str(len(Place.objects.all()) + 1)
                    new_place.save()

                    for position, picture in enumerate(response.json()["imgs"]):
                        new_response = requests.get(picture)
                        photo = Photo.objects.get_or_create(
                            position=position,
                            place=new_place,
                        )
                        photo[0].image.save(
                            f"{picture.split('/media/')[-1]}",
                            ContentFile(new_response.content),
                            save=True
                        )
        except TypeError:
            print("Type error")
