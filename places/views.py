from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse

from places.models import Place


def get_locations():
    locations = Place.objects.all()
    locations_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place.coordinates_lon,
                        place.coordinates_lat
                    ]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.placeId,
                    "detailsUrl": reverse(
                        place_detail_view,
                        args=[place.placeId]
                    ),
                }
            } for place in locations
        ]
    }
    return locations_json


def place_detail_view(request, place_id):
    place = Place.objects.filter(placeId=place_id).first()

    place_json = {
        "title": place.title,
        "imgs": [
           img.image.url for img in list(
                place.photos.all().order_by("position")
            )
        ],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.coordinates_lon,
            "lat": place.coordinates_lat,
        }
    }
    return JsonResponse(
        place_json,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 4}
    )


def main_page(request):

    locations = get_locations()

    template = loader.get_template("index.html")
    context = {"locations": locations}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
