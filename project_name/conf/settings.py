# Import global settings to make it easier to extend settings.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from .paths import PROJECT_DIR, PROJECT_NAME, VAR_ROOT
import os
import milieu

M = milieu.init()

# ==============================================================================
# Generic Django project settings
# ==============================================================================
DEBUG = M.DEBUG or False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'GMT'
USE_I18N = True
SITE_ID = 1

SECRET_KEY = M.SECRET_KEY

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

ADMINS = (
    ('Administrator', M.ADMIN_EMAIL or "admin@unholster.com"),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = (M.ALLOWED_HOSTS,)

# ==============================================================================
# Project URLS and media settings
# ==============================================================================

ROOT_URLCONF = PROJECT_NAME + '.conf.urls'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'


# =============================================================================
# Static files and frontend
# =============================================================================
FRONT_BUILD_DIR = 'static'
STATIC_DOMAIN = M.STATIC_DOMAIN
STATIC_URL = M.STATIC_URL or ('/static/%s/' % PROJECT_NAME)
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_NAME, FRONT_BUILD_DIR),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = M.MEDIA_URL or ('/uploads/%s/' % PROJECT_NAME)
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')


# ==============================================================================
# Middlewares
# ==============================================================================
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# ==============================================================================
# Templates
# ==============================================================================
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
)

# =============================================================================
# Databases
# =============================================================================
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=M.DATABASE_URL)}

# =============================================================================
# Caching
# =============================================================================
if M.MEMCACHE_SERVERS:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': M.MEMCACHE_SERVERS,
            'TIMEOUT': 0,
            'BINARY': True,
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

CACHES['staticfiles'] = {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'staticfiles'
}

# =============================================================================
# Apps
# =============================================================================
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'password_reset',
    'bootstrapform',
    'frontflow',
)

# =============================================================================
# Logging
# =============================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'  # noqa
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        PROJECT_NAME: {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
