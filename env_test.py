import os

DEBUG = os.getenv('DJANGO_DEBUG', True)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
DB_PATH = os.getenv('DJANGO_DATABASE_PATH')
STATIC_FILE_PATH = os.getenv('DJANGO_STATIC_PATH')
MEDIA_FILE_PATH = os.getenv('DJANGO_MEDIA_PATH')
