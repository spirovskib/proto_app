#!/bin/sh

echo "Running migrations."
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations application
python manage.py migrate

echo "Checking for superuser and creating one if no users exist."
echo "from django.contrib.auth import get_user_model; User = get_user_model()\nif not User.objects.exists(): User.objects.create_superuser('shodan@trioptimum.com', 'RickenbackerVonBraun')" | python manage.py shell

echo "Collecting static files."
python manage.py collectstatic --noinput

echo "Starting servers."
/usr/bin/supervisord