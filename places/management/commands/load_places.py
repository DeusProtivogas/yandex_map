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

                formatted_response = response.json()

                new_place, created = Place.objects.get_or_create(
                    title=formatted_response["title"],
                    defaults={
                        "short_description": formatted_response["description_short"],
                        "long_description": formatted_response["description_long"],
                        "coordinates_lon": formatted_response["coordinates"]["lng"],
                        "coordinates_lat": formatted_response["coordinates"]["lat"],
                    }
                )
                if created:

                    for position, picture in enumerate(response.json()["imgs"]):
                        new_response = requests.get(picture)
                        photo = Photo.objects.get_or_create(
                            position=position,
                            place=new_place,
                            image=ContentFile(
                                content=new_response.content,
                                name=f"{picture.split('/media/')[-1]}"
                            ),
                        )
                else:
                    print("Place already exists!")
        except requests.exceptions.MissingSchema:
            print("Invalid URL")
        except TypeError:
            print("Type error")
