from dotenv import load_dotenv, find_dotenv
# Activates env automatically with dev_settings.

load_dotenv(find_dotenv())

from .settings import *  # noqa

DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions'
)
