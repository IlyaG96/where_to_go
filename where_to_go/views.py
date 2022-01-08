from django.shortcuts import render
from places.models import Post, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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


def places(request, post_id):
    current_post = get_object_or_404(Post.objects.filter(id=post_id))
    return HttpResponse(current_post.title)
