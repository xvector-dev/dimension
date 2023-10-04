#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input

gunicorn server.wsgi:application --bind 0.0.0.0:8081 &

unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;'
