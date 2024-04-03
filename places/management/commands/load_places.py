import requests
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Photo

class Command(BaseCommand):
    help = 'Add more locations to the database'

    def add_arguments(self, parser):
        parser.add_argument('json_address', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for address in options['json_address']:
                print(address)
                r = requests.get(address,)
                print(r.status_code)
                # print(r.json())

                new_place, created = Place.objects.get_or_create(
                    title = r.json()['title'],
                    short_description =r.json()['description_short'],
                    long_description = r.json()['description_long'],
                    coordinates_lon = r.json()['coordinates']['lng'],
                    coordinates_lat = r.json()['coordinates']['lat'],
                )
                if created:
                    new_place.placeId = str(len(Place.objects.all()) + 1)
                    new_place.save()

                    for pos, p in enumerate(r.json()['imgs']):
                        new_r = requests.get(p)
                        # print(new_r.content)
                        # photo_upload = Image.open(BytesIO(new_r.content)).save(f"{p.split('/media/')[-1]}")
                        photo = Photo.objects.get_or_create(
                            position=pos,
                            # upload=photo_upload,
                            place=new_place,
                        )
                        photo[0].upload.save(f"{p.split('/media/')[-1]}", ContentFile(new_r.content), save=True)
                        # print(i)
                        # break
        except TypeError:
            print("Type error")
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
    #
    # def handle(self, *args, **options):
    #     for poll_id in options['poll_ids']:
    #         try:
    #             poll = Poll.objects.get(pk=poll_id)
    #         except Poll.DoesNotExist:
    #             raise CommandError('Poll "%s" does not exist' % poll_id)
    #
    #         poll.opened = False
    #         poll.save()
    #
    #         self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
