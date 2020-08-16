#!/bin/sh

python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations application
python manage.py migrate

python manage.py collectstatic --noinput

/usr/bin/supervisord