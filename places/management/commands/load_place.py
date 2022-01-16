import django
import os
import requests
import argparse
from pathlib import Path
from places.models import Post, Image
from urllib.parse import urlparse, unquote
from django.core.management.base import BaseCommand


def get_json():
    url = "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Лагерь%20«Подмосковный».json"
    response = requests.get(url)
    response.raise_for_status()
    description = response.json()

    return description


def get_filename_from_photo_link(image):

    file_name_index = 1
    path_to_file = urlparse(image).path
    file_name = unquote(path_to_file)
    file_name = os.path.split(file_name)[file_name_index]

    return file_name


def download_image(image, title):
    response = requests.get(image)
    response.raise_for_status()
    filename = get_filename_from_photo_link(image)
    path_to_file = f"../../media/{title}/{filename}"
    if not Path(path_to_file).is_file():
        with open(file=path_to_file, mode="wb") as file:
            file.write(response.content)

def write_data_to_db(description):

    description_short = description["description_short"]
    description_long = description["description_long"]
    longitude = description["coordinates"]["lng"]
    latitude = description["coordinates"]["lat"]
    images_links_from_json = description["imgs"]
    title = description["title"]

    Path(f"../../media/{title}").mkdir(parents=True, exist_ok=True)

    Post.objects.get_or_create(title=title,
                               description_long=description_long,
                               description_short=description_short,
                               longitude=longitude,
                               latitude=latitude
                               )
    current_post = Post.objects.get(title=title)
    for image in images_links_from_json:
        Image.objects.create(post=current_post,
                             image=download_image(image, title))

    imgs = [image.image.url for image in current_post.image.all()]

    Post.objects.update(imgs=imgs)


def main():
  #  parser = argparse.ArgumentParser(
  #      description="Позволяет загружать JSON либо с сервера, либо из локальной директории"
  #  )
  #  parser.add_argument("json_path",
  #                      help="Путь к json файлу",
  #                      type=int,
  #                      default=1,
  #                      nargs="?")
  #  args = parser.parse_args()

    get_json()
    description = get_json()
    write_data_to_db(description)


class Command(BaseCommand):
    help = "123"

    def handle(self, *args, **options):
        main()

