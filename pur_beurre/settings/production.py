from . import *


SECRET_KEY = os.getenv('DJANGO_KEY')
DEBUG = False
ALLOWED_HOSTS = ['167.99.142.3']
ROOT_URLCONF = os.getenv('ROOT_URLCONF')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # we use the postgresql adaptator
        'NAME': os.getenv('POSTGRESQL_DB_NAME'),
        'USER': os.getenv('POSTGRESQL_USER'),
        'PASSWORD': os.getenv('POSTGRESQL_PSWD'),
        'HOST': '',
        'PORT': '5432',
    }
}
