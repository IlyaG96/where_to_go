from django.shortcuts import render
from places.models import Point
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.html import format_html, mark_safe
from django.urls import reverse_lazy


def serialize_content(point):
    return {
        "type": "Feature",
        "geometry": {"type": "Point",
                     "coordinates": [point.longitude, point.latitude]
                     },
        "properties": {
            "title": point.title,
            "placeId": point.id,
            "detailsUrl": reverse_lazy('places', args=[point.id])
        }
    }


def index_page(request):
    all_points = Point.objects.all().only("longitude", "latitude", "title", "id")
    content = {
        "type": "FeatureCollection",
        "features": [serialize_content(point) for point in all_points]
    }
    context = {"content": content}
    return render(request, 'index.html', context)


def places(request, point_id):
    try:
        current_point = Point.objects.get(id=point_id)
    except Point.DoesNotExist:

        content = ('<html>'
                   '<body>'
                   'Такого места еще не существует'
                   '<p><a href = "/">На главную</a></p>'
                   '</body>'
                   '</html>')

        response = format_html(mark_safe(content))
        return HttpResponse(response)

    title = current_point.title
    description_short = current_point.description_short
    description_long = current_point.description_long
    longitude = current_point.longitude
    latitude = current_point.latitude
    images = [image.image.url for image in current_point.images.all()]
    response_data = {
        "title": title,
        "imgs": images,
        "description_short": description_short,
        "description_long": description_long,
        "coordinates": {
            "lon": longitude,
            "lat": latitude
        }
    }
    return JsonResponse(response_data,
                        safe=False,
                        json_dumps_params={"ensure_ascii": True, "indent": 2})
