from django.shortcuts import render
from places.models import Post
from django.http import JsonResponse
from django.http import HttpResponse

def serialize_content(post):
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
        "features": [serialize_content(post) for post in all_posts]
    }
    context = {"json": content}
    return render(request, 'index.html', context)


def places(request, post_id):
    try:
        current_post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        response = ('<html>'
                    '<body>'
                    'Такого места еще не существует'
                    '<p><a href = "/">На главную</a></p>'
                    '</body>'
                    '</html>')
        return HttpResponse(response)

    title = current_post.title
    description_short = current_post.description_short
    description_long = current_post.description_long
    longitude = current_post.longitude
    latitude = current_post.latitude
    images = [image.image.url for image in current_post.images.all()]
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
