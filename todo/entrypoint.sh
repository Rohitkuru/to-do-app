#!/bin/sh

python manage.py migrate

python manage.py collectstatic --no-input

gunicorn todo.wsgi:application --bind 0.0.0.0:8000 --workers 5