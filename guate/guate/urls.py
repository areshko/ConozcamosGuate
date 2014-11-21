from django.conf.urls import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from principal.views import archive
from principal.views import archiveDepartamentos
from principal.views import archiveMunicipios
from principal.views import *
from django.conf.urls import url 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guate.views.home', name='home'),
    #url(r'^$', include('principal.urls')),
    #url(r'^proyecto/principal', include('principal.urls')),
    url(r'^departamentos/$', 'principal.views.archiveDepartamentos', name ='archiveDepartamentos'),
    url(r'^municipios/$', 'principal.views.archiveMunicipios', name ='archiveMunicipios'),
    url(r'^eventos/$', 'principal.views.archive', name ='archive'),
    url(r'^insdep/$', 'principal.views.formularioDepartamento', name='formularioDepartamento'),
    url(r'^insevent/$', 'principal.views.formularioEvento', name='formularioEvento'),
    url(r'^insmuni/$', 'principal.views.formularioMunicipio', name='formularioMunicipio'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^codigofacilito/admin/', include(admin.site.urls)),
)
