from django.conf.urls import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from principal.views import archive
from principal.views import archiveDepartamentos
from principal.views import *
from django.conf.urls import url 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codigofacilito.views.home', name='home'),
    url(r'^$', archive),
    url(r'^$', archiveMunicipios),
    url(r'^hola/$', archiveDepartamentos),   
)