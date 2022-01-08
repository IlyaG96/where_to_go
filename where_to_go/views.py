from django.shortcuts import render
from places.models import Post, Image
from django.http import HttpResponse
from django.template import loader
from django.utils.safestring import SafeString
from django.http import JsonResponse
from django.forms.models import model_to_dict
from json import dumps


def serialize_post(post):
    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": list(post.coordinates.values())},
        "properties": {
            "title": post.title,
            "placeId": post.id,
            "detailsUrl": post.details_url
        }
    }


def index_page(request):
    all_posts = Post.objects.all()
    content = {
        "type": "FeatureCollection",
        "features": [serialize_post(post) for post in all_posts]
    }
    context = {"json": content}
    return render(request, 'index.html', context)

