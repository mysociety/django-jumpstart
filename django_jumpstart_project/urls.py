from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_jumpstart_project.views.home', name='home'),
    # url(r'^django_jumpstart_project/', include('django_jumpstart_project.foo.urls')),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# serve media_root files (only works when DEBUG is True)
# https://docs.djangoproject.com/en/1.3/howto/static-files/#django.conf.urls.static.static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
