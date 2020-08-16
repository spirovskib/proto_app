#!/bin/sh


FILE=$DJANGO_DATABASE_PATH/db.sqlite3
if [ -f "$FILE" ]; then
    SUPER=False
else
    SUPER=True
fi

python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations application
python manage.py migrate

if [ $SUPER ='True']; then
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@example.com', 'Password1$')" | python manage.py shell
fi
python manage.py collectstatic --noinput

/usr/bin/supervisord