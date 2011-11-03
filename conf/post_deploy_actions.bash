#!/bin/bash

# abort on any errors
set -e

# check that we are in the expected directory
cd `dirname $0`/..

# create/update the virtual environment

# NOTE: some packages are difficult to install if they are not site packages,
# for example xapian. If using these you might want to add the
# '--enable-site-packages' argument.
pip install \
    --environment ../django-jumpstart-virtualenv \
    --requirement requirements.txt \
    --quiet

# use the virtualenv just created/updated
source ../django-jumpstart-virtualenv/bin/activate

# make sure that there is no old code (the .py files may have been git deleted) 
find . -name '*.pyc' -delete

# go to the project directory for local config
cd ./django_jumpstart_project

# get the database up to speed
./manage.py syncdb
./manage.py migrate

# gather all the static files in one place
./manage.py collectstatic --noinput

cd --
