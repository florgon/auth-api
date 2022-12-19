# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv/www/florgon/api

# Install requirements.
RUN apk add build-base
RUN pip install --upgrade pip
COPY api/requirements-testing.txt /srv/www/florgon/api/
RUN pip install --upgrade --no-cache-dir -r requirements-testing.txt

COPY . /srv/www/florgon/api/
CMD ["gunicorn", "app.app:app", "-c", "gunicorn.conf.py"]