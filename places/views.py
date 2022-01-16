from django.shortcuts import render
from places.models import Post
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json


def serialize_post(post):
    return {
        "type": "Feature",
        "geometry": {"type": "Point",
                     "coordinates": [post.longitude, post.latitude]
                     },
        "properties": {
            "title": post.title,
            "placeId": post.id,
            "detailsUrl": f"places/{post.id}"
        }
    }


def index_page(request):
    all_posts = Post.objects.all().only("longitude", "latitude", "title", "id")
    content = {
        "type": "FeatureCollection",
        "features": [serialize_post(post) for post in all_posts]
    }
    context = {"json": content}
    return render(request, 'index.html', context)


def places(request, post_id):
    current_post = get_object_or_404(Post.objects.filter(id=post_id))
    title = current_post.title
    description_short = current_post.description_short
    description_long = current_post.description_long
    longitude = current_post.longitude
    latitude = current_post.latitude
    images = [image.image.url for image in current_post.image.all()]
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
