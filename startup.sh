#!/bin/sh

# Eventually refactor how migrations are hadled
# Perhaps follow: https://pythonspeed.com/articles/schema-migrations-server-startup/
alembic upgrade head

gunicorn app.app:app --bind 0.0.0.0
