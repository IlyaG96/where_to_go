from django.shortcuts import render
from places.models import Post, Image
from django.http import HttpResponse
from django.template import loader
from django.utils.safestring import SafeString
from django.http import JsonResponse
from django.forms.models import model_to_dict
from json import dumps


def serialize_post(post):
    pass


def index_page(request):
    # all_posts = Post.objects.all()
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
                }
            }
        ]
    }

    context = {"json": data}
    return render(request, 'index.html', context)
