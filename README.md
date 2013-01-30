This project is intended to be a template to base mySociety Django projects on.
It is not meant to be deployable on its own.

Set up from a fresh empty repository:

    $ cd <path-to-parent-of-where-you-want-to-clone-django-jumpstart>
    $ git clone https://github.com/mysociety/django-jumpstart
    $ cd <path-to-your-new-project-dir>
    $ VIRTUALENV_PATH=../virtualenv-project
    $ virtualenv --no-site-packages $VIRTUALENV_PATH
    $ source $VIRTUALENV_PATH/bin/activate
    $ pip install Django
    $ django-admin.py startproject --template=<path-to-django-jumpstart>/project_template --extension py,yml,bash,conf-example,yml-example project_name .
    $ pip install -r requirements.txt

You will need to edit the .gitignore to ignore the normal deployed general and
httpd.conf files.

You might want to think about adding commonlib as a submodule.

Then when adding an app, use:

    ./manage.py startapp --template=<path-to-app_template-directory> app_name

Possible todo
-------------

* mySociety banner to the header/footer
* 404 and 500 templates

