#!/bin/sh

# echo "Waiting for postgres..."

# while ! nc -z db 5432; do
#   sleep 2
# done

# echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata auth

exec "$@"
