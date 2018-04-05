#!/bin/sh
python /app/manage.py collectstatic --noinput
/usr/local/gunicorn conf.wsgi -c file:/gunicorn_config.py --chdir=/app
