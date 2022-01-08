from django.shortcuts import render
from places.models import Post, Image
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
import json


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


def places(post_id):
    current_post = get_object_or_404(Post.objects.filter(id=post_id))
    title = current_post.title
    description_short = current_post.description_short
    description_long = current_post.description_long
    coordinates = current_post.coordinates
    images = Image.objects.filter(post=current_post)
    imgs = [image.image.url for image in images]
    response_data = {
        "title": title,
        "imgs": imgs,
        "description_short": description_short,
        "description_long": description_long,
        "coordinates": coordinates
    }

    return HttpResponse(json.dumps(response_data, ensure_ascii=True, indent=2),
                        content_type="application/json")
