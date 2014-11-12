from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('unholster.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
