from . import *


SECRET_KEY = os.getenv('DJANGO_KEY')
DEBUG = False
ALLOWED_HOSTS = ['167.99.142.3']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # we use the postgresql adaptator
        'NAME': 'purbeurre',
        'USER': os.getenv('POSTGRESQL_USER'),
        'PASSWORD': os.getenv('POSTRESQL_PSWD'),
        'HOST': '',
        'PORT': '5432',
    }
}
