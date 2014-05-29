from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
from django.contrib.staticfiles.storage import CachedFilesMixin
from django.conf import settings

class CachedS3Storage(CachedFilesMixin, S3BotoStorage):
    pass

StaticStorage = lambda: CachedS3Storage(location=settings.STATIC_URL, custom_domain=settings.STATIC_DOMAIN)
MediaStorage  = lambda: S3BotoStorage(location='media', headers={
        'Cache-Control': 'max-age=2147483648',
    })