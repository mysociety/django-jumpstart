This project is intended to be a template to base mySociety Django projects on.
It is not meant to be deployable on its own.

Set up from a fresh empty repository:

$ VIRTUALENV_PATH=../virtualenv-project
$ virtualenv --no-site-packages $VIRTUALENV_PATH
$ source $VIRTUALENV_PATH/bin/activate
$ pip install Django
$ django-admin.py startproject --template=<path-to-project_template-directory> --extension py,yml,bash,conf-example,yml-example project_name .
$ pip install -r requirements.txt

You might want to think about adding commonlib as a submodule.

Then when adding an app, use
./manage.py startapp --template=<path-to-app_template-directory> app_name
