import os
import requests
import traceback
from pathlib import Path
from places.models import Point, Image
from urllib.parse import urlparse, unquote
from django.core.management.base import BaseCommand


def get_filename_from_photo_link(image):
    file_name_index = 1
    path_to_file = urlparse(image).path
    file_name = unquote(path_to_file)
    file_name = os.path.split(file_name)[file_name_index]

    return file_name


def write_to_db(place_description):
    description_short = place_description["description_short"]
    description_long = place_description["description_long"]
    longitude = place_description["coordinates"]["lng"]
    latitude = place_description["coordinates"]["lat"]
    images_links_from_json = place_description["imgs"]
    title = place_description["title"]

    Path(f"./media/{title}").mkdir(parents=True, exist_ok=True)

    current_point, created = (Point.objects.
                              get_or_create(title=title,
                                            description_long=description_long,
                                            description_short=description_short,
                                            longitude=longitude,
                                            latitude=latitude
                                            ))
    for link in images_links_from_json:
        response = requests.get(link)
        response.raise_for_status()
        filename = get_filename_from_photo_link(link)
        path_to_file = f"./media/{title}/{filename}"
        with open(file=path_to_file, mode="wb+") as file:
            file.write(response.content)
            image = Image(point=current_point)
            image.image.save(filename, file)
            Path(path_to_file).unlink()
    images_links = [image.image.url for image in current_point.images.all()]
    current_point.imgs = images_links
    current_point.save()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-u", "--json_url", required=True)

    def handle(self, *args, **options):
        url = options["json_url"]

        try:
            response = requests.get(url)
            response.raise_for_status()
            place_description = response.json()
            write_to_db(place_description)
        except requests.exceptions.HTTPError:
            traceback.print_exc()
            print("Не удалось загрузить json с указанного адреса")
