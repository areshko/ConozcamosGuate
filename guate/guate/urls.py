from django.conf.urls import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guate.views.home', name='home'),
    url(r'^$', include('principal.urls')),
    url(r'^proyecto/principal', include('principal.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^codigofacilito/admin/', include(admin.site.urls)),
)
