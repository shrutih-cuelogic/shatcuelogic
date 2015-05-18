from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^tango_with_django_project/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT,}),
)

