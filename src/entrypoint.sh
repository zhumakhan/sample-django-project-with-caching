#!/bin/bash

case "$MODE" in
"TEST")
    echo "TEST"
    # python manage.py migrate && \
    # pytest -v --cov . --cov-report term-missing --cov-fail-under=100 \
    # --flake8 --color=yes -n 4 --no-migrations --reuse-db -W error
    ;;
"PROD")
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations --noinput&& \
    python manage.py migrate && \
    uwsgi --ini deploy.ini
    ;;
"DEV")
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations --noinput && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
    ;;
"CELERY")
    rm -f celerybeat-schedule && \
    celery -A core worker --beat --loglevel=INFO
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
