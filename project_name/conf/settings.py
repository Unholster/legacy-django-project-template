# Import global settings to make it easier to extend settings.

from .paths import PROJECT_DIR, PROJECT_NAME, VAR_ROOT, E
import os

# ==============================================================================
# Generic Django project settings
# ==============================================================================
DEBUG = E.DEBUG or False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'GMT'
USE_I18N = True
SITE_ID = 1

SECRET_KEY = E.SECRET_KEY

VAR_ROOT = E.VAR_ROOT or VAR_ROOT ## Var root can be overriden

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

ADMINS = (
    ('Administrator', E.ADMIN_EMAIL or "admin@unholster.com"),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = '*'

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
STATIC_DOMAIN = E.STATIC_DOMAIN
STATIC_URL = E.STATIC_URL or ('/static/%s/' % PROJECT_NAME)

STATIC_ROOT = E.STATIC_ROOT or os.path.join(VAR_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_NAME, FRONT_BUILD_DIR),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = E.MEDIA_URL or ('/uploads/%s/' % PROJECT_NAME)
MEDIA_ROOT = E.MEDIA_ROOT or os.path.join(VAR_ROOT, 'uploads')


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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, PROJECT_NAME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =============================================================================
# Databases
# =============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': E.DATABASE_NAME,
        'USER': E.DATABASE_ROLE,
        'PASSWORD': E.DATABASE_PASSWORD,
        'HOST': E.DATABASE_HOST,
        'PORT': E.DATABASE_PORT or '5432',
    }
}

# =============================================================================
# Caching
# =============================================================================
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': E.CACHE_URL or 'redis://localhost:6379/0',
    }, 'staticfiles': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'staticfiles',
    }, 'template_cache': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': E.TEMPLATE_CACHE_URL or 'redis://localhost:6379/9',
    }
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
    'channels',
    'rest_framework_swagger',
    'rest_framework',
    '{{project_name}}.apps.base',
    'django_celery_beat',
)

# =============================================================================
# Logging
# =============================================================================
LOG_DIR = E.LOG_DIR or os.path.join(VAR_ROOT, 'log')
os.makedirs(LOG_DIR, mode=0o777, exist_ok=True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'dev_friendly': {
            'format': '[%(levelname)7s] %(asctime)s  %(name)20s %(lineno)3d | %(message)s'  # noqa
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            # noqa
        },
    },
    'handlers': {
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'base_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev_friendly'
        },
        'commands': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'commands.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'request_handler'],
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'base_handler'],
    },
}

# =============================================================================
# Celery
# =============================================================================

BROKER_URL = E.CELERY_URL or 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = BROKER_URL or 'redis://localhost:6379/1'
CELERYD_MAX_TASKS_PER_CHILD = E.CELERYD_MAX_TASKS_PER_CHILD or 1
BROKER_POOL_LIMIT = E.CELERY_POOL_LIMIT or 0


# =============================================================================
# CHANNELS
# =============================================================================


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.environ.get('REDIS_HOST', 'localhost'), 6379)],
        },
        "ROUTING": "{{project_name}}.apps.base.routing.channel_routing",
    },
}

# =============================================================================
# REST_FRAMEWORK
# =============================================================================


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}

JWT_AUTH = {
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=5),
    'JWT_ALLOW_REFRESH': True,
}
