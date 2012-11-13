# load the mySociety config from its special file

import yaml
from .paths import *

config = yaml.load(open(os.path.join(PROJECT_ROOT, 'conf', 'general.yml')))

DEBUG = bool(int(config.get('STAGING')))
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('{{ project_name|upper }}_DB_NAME'),
        'USER': config.get('{{ project_name|upper }}_DB_USER'),
        'PASSWORD': config.get('{{ project_name|upper }}_DB_PASS'),
        'HOST': config.get('{{ project_name|upper }}_DB_HOST'),
        'PORT': config.get('{{ project_name|upper }}_DB_PORT'),
    }
}

TIME_ZONE = config.get('TIME_ZONE')
SECRET_KEY = config.get('DJANGO_SECRET_KEY')
GOOGLE_ANALYTICS_ACCOUNT = config.get('GOOGLE_ANALYTICS_ACCOUNT')
