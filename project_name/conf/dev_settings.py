from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions'
)