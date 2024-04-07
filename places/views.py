from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from places.models import Place


def get_locations():
    locations = Place.objects.all()
    return {
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


def place_detail_view(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related("photos"), placeId=place_id)

    place_json = {
        "title": place.title,
        "imgs": [
           img.image.url for img in place.photos.all().order_by("position")
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
    return render(request, "index.html", context={"locations": locations})
