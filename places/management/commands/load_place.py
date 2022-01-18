import json

import django
import os
import requests
import argparse
from pathlib import Path
from places.models import Post, Image
from urllib.parse import urlparse, unquote
from django.core.management.base import BaseCommand


def get_json(url):
    response = requests.get(url)
    response.raise_for_status()
    description = response.json()

    return description


def open_json(path):
    with open(file=path, mode="r") as file:
        description = json.load(file)
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
    path_to_file = f"./media/{title}/{filename}"
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

    Path(f"./media/{title}").mkdir(parents=True, exist_ok=True)

    Post.objects.get_or_create(title=title,
                               description_long=description_long,
                               description_short=description_short,
                               longitude=longitude,
                               latitude=latitude
                               )

    current_post = Post.objects.get(title=title)
    for image in images_links_from_json:
        response = requests.get(image)
        response.raise_for_status()
        filename = get_filename_from_photo_link(image)
        path_to_file = f"./media/{title}/{filename}"
        if not Path(path_to_file).is_file():
            with open(file=path_to_file, mode="wb+") as file:
                file.write(response.content)
                images = Image(post=current_post)
                images.image.save(filename, file, save=True)
            Path(path_to_file).unlink()
    imgs = [image.image.url for image in current_post.images.all()]
    current_post.imgs = imgs
    current_post.save()


def main():
    parser = argparse.ArgumentParser(
        description="Позволяет загружать JSON либо с сервера, либо из локальной директории"
    )
    parser.add_argument("-json_path",
                        help="Путь к json файлу",
                        nargs="?")
    parser.add_argument("-json_folder",
                        help="Путь к json файлу",
                        nargs="?")
    args = parser.parse_args()
    if args.json_path:
        if "http" in args.json_path:
            description = get_json(args.json_path)
        else:
            description = open_json(args.json_path)

        write_data_to_db(description)
    else:
        for jsons in args.json_folder:  # not working at all
            description = open_json(args.json_path)
            write_data_to_db(description)


class Command(BaseCommand):
    help = "Add information from json file to db"

    def add_arguments(self, parser):

        parser.add_argument("-json_path",
                        help="Путь к json файлу",
                        nargs="?")
        parser.add_argument("-json_folder",
                        help="Путь к json файлу",
                        nargs="?")

    def handle(self, *args, **options):
        print(args)
        main()


"Users/ilyagabdrakhmanov/PycharmProjects/where_to_go/json/Антикафе\ Bizone.json"
