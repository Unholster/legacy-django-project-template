import os, sys
import site
from conf.paths import *

site.addsitedir('%s/lib/python%d.%d/site-packages' % (PROJECT_DIR, sys.version_info[0], sys.version_info[1]))
sys.stdout = sys.stderr

if os.getenv('DEBUG', False):
    settings_module = '%s.conf.dev.settings'
else:
    settings_module = '%s.conf.settings'
    
os.environ['DJANGO_SETTINGS_MODULE'] = settings_module % PROJECT_NAME

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()