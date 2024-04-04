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
                print(address)
                r = requests.get(address,)
                print(r.status_code)

                new_place, created = Place.objects.get_or_create(
                    title = r.json()["title"],
                    short_description =r.json()["description_short"],
                    long_description = r.json()["description_long"],
                    coordinates_lon = r.json()["coordinates"]["lng"],
                    coordinates_lat = r.json()["coordinates"]["lat"],
                )
                if created:
                    new_place.placeId = str(len(Place.objects.all()) + 1)
                    new_place.save()

                    for pos, p in enumerate(r.json()["imgs"]):
                        new_r = requests.get(p)
                        photo = Photo.objects.get_or_create(
                            position=pos,
                            # upload=photo_upload,
                            place=new_place,
                        )
                        photo[0].image.save(f"{p.split('/media/')[-1]}", ContentFile(new_r.content), save=True)
        except TypeError:
            print("Type error")
