#!/bin/bash

# abort on any errors
set -e

# create/update the virtual environment
pip install \
    -q \
    -E ../django-jumpstart-virtualenv \
    -r requirements.txt

# use the virtualenv just created/updated
source ../django-jumpstart-virtualenv/bin/activate

# go to the project directory for local config
cd ./django_jumpstart_project

# make sure that there is no old code (the .py files may have been git deleted) 
find . -name '*.pyc' -delete

# get the database up to speed
./manage.py syncdb
./manage.py migrate

# gather all the static files in one place
./manage.py collectstatic --noinput

cd --
