#!/bin/sh

alembic upgrade head

gunicorn skatebase.app:app --bind 0.0.0.0
