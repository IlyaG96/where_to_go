import requests
import argparse
from pathlib import Path
from where_to_go import settings
from pprint import pprint
from places.models import *
from urllib.parse import urlparse, unquote
import os


def get_json(args):
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
    print(file_name)

    return file_name


def download_images(images, title):
    for image in images:
        response = requests.get(image)
        response.raise_for_status()
        filename = get_filename_from_photo_link(image)
        with open(file=f"../../media/{title}/{filename}", mode="wb") as file:
            file.write(response.content)


def write_data_to_db(description):

    # images = [image.image.url for image in current_post.image.all()]
    title = description["title"]
    description_short = description["description_short"]
    description_long = description["description_long"]
    imgs = description["imgs"]
    title = description["title"]
    Path(f"../../media/{title}").mkdir(parents=True, exist_ok=True)
    download_images(imgs, title)


def main():
    parser = argparse.ArgumentParser(
        description="Позволяет загружать JSON либо с сервера, либо из локальной директории"
    )
    parser.add_argument("json_path",
                        help="Путь к json файлу",
                        type=int,
                        default=1,
                        nargs="?")
    args = parser.parse_args()

    get_json(args)
    description = get_json(args)
    write_data_to_db(description)


if __name__ == '__main__':
    main()

"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        main()"""