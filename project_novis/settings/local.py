import socket

from setuptools_scm import get_version

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "INSECURE")

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost'
        }
}

CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
