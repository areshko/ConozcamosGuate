from django.conf.urls import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from principal.views import archive
from principal.views import archiveDepartamentos
from principal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codigofacilito.views.home', name='home'),
    url(r'^$', archiveMunicipios),
    url(r'^$', archive),
    url(r'^hola/$', archiveDepartamentos),
    
)