from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    # project urls here
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include('django.contrib.admin.site.urls')),
)