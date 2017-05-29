import raven

from .settings import *  # noqa

ALLOWED_HOSTS = M.ALLOWED_HOSTS
# ==============================================================================
# SENTRY
# ==============================================================================
if M.RAVEN_DSN:
    RAVEN_CONFIG = {
        'dsn': M.RAVEN_DSN,
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    }
    INSTALLED_APPS = INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',
    )

    MIDDLEWARE_CLASSES += (
        'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
        'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',  # NOQA
    )

    LOGGING['handlers']['sentry'] = {
        'level': M.SENTRY_LOGLEVEL or 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        'tags': {'custom-tag': 'x'},
    }

    LOGGING['loggers']['sentry.errors'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False,
    }

    LOGGING['loggers']['celery'] = {
        'level': 'WARNING',
        'handlers': ['sentry'],
        'propagate': False,
    }

    LOGGING['root']['handlers'].append('sentry')

# ==============================================================================
# PAPERTRAIL
# ==============================================================================
if M.PAPERTRAIL_URL and M.PAPERTRAIL_PORT:
    LOGGER_NAME = '{{project_name}}'.upper()
    LOGGING['handlers']['PaperTrail'] = {
        'level': 'DEBUG',
        'class': 'logging.handlers.SysLogHandler',
        'formatter': 'papertrail',
        'address': (M.PAPERTRAIL_URL, int(M.PAPERTRAIL_PORT))
    }
    LOGGING['formatters']['papertrail'] = {
        'format': f'%(asctime)s {LOGGER_NAME} %(name)s %(levelname)s %(message)s',
        'datefmt': '%Y-%m-%dT%H:%M:%S',
    }
    LOGGING['root']['handlers'].append('PaperTrail')
