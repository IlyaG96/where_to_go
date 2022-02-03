import os
import json
import requests
import traceback
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


def write_to_db(place_description):
    description_short = place_description["description_short"]
    description_long = place_description["description_long"]
    longitude = place_description["coordinates"]["lng"]
    latitude = place_description["coordinates"]["lat"]
    images_links_from_json = place_description["imgs"]
    title = place_description["title"]

    Path(f"./media/{title}").mkdir(parents=True, exist_ok=True)

    current_post, created = (Post.objects.
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
        if not Path(path_to_file).is_file():
            with open(file=path_to_file, mode="wb+") as file:
                file.write(response.content)
                image = Image(post=current_post)
                image.image.save(filename, file)
            Path(path_to_file).unlink()
    imgs = [image.image.url for image in current_post.images.all()]
    current_post.imgs = imgs
    current_post.save()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-u', '--json_url')
        parser.add_argument('-p', '--json_path')

    def handle(self, *args, **options):
        url = options['json_url']
        path = options['json_path']

        if not url and not path:
            print('Ни путь к файлу, ни url не заданы')

        elif path:

            try:
                place_description = open_json(path)
                write_to_db(place_description)
            except FileNotFoundError:
                traceback.print_exc()
                print(f'\nФайл по пути {path} не найден')

        elif url:
            try:
                place_description = get_json(url)
                write_to_db(place_description)
            except Exception as exception:
                print(f'{exception}\n'
                      f'Не удалось загрузить json с указанного адреса')
