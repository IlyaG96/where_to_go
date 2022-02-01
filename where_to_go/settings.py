"""
Django settings for where_to_go project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django

from pathlib import Path
import os
from environs import Env
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])
SECRET_KEY = env.str('SECRET_KEY', 'REPLACE_ME')
DEBUG = env.bool('DEBUG', True)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'places',
    'adminsortable2',
    "debug_toolbar",
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

ROOT_URLCONF = 'where_to_go.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'where_to_go.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = 'media/'
MEDIA_DIRS = [
    os.path.join(BASE_DIR, "media")
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    "127.0.0.1",
]
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'height': 300,
    'menubar': True,
    'plugins': 'advlist,autolink,lists,link,image,charmap,print,preview,anchor,'
               'searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,'
               'code,help,wordcount',
    'toolbar': 'undo redo | formatselect | '
               'bold italic backcolor | alignleft aligncenter '
               'alignright alignjustify | bullist numlist outdent indent | '
               'removeformat | help',
}

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")
django.setup()
