import os

import logging
import raven
import celery
from raven.contrib.celery import register_signal, register_logger_signal

PROJECT_NAME = '{{project_name}}'

os.environ.setdefault('DJANGO_ENV', 'dev')
DJANGO_ENV = os.environ['DJANGO_ENV']

settings_module = '%s.conf.%s_settings' % (PROJECT_NAME, DJANGO_ENV)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

app = celery.Celery('conf')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
if os.environ.get('RAVEN_DSN'):
    client = raven.Client(dsn=os.environ.get('RAVEN_DSN'))

    # register a custom filter to filter out duplicate logs
    register_logger_signal(client)

    # The register_logger_signal function can also take an optional argument
    # `loglevel` which is the level used for the handler created.
    # Defaults to `logging.ERROR`
    register_logger_signal(client, loglevel=logging.INFO)

    # hook into the Celery error handler
    register_signal(client)

    # The register_signal function can also take an optional argument
    # `ignore_expected` which causes exception classes specified in Task.throws
    # to be ignored
    register_signal(client, ignore_expected=True)
