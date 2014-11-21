from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Departamento(models.Model):
	nombreDepartamento = models.CharField(max_length=45)

	def nombreDepartamento_upper(self):
		return ("%s" % (self.nombreDepartamento)).upper()

	nombreDepartamento_upper.short_description = "Departamento"

class  DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('nombreDepartamento',)

class Municipio(models.Model):
	nombreMunicipio = models.CharField(max_length=45)
	iddepartamento = models.ForeignKey('Departamento')
    #def __str__(self):
        #return self.nombreMunicipio
    #__str__ = 'Titulo'

	#def upper_case_iddepartamento(self, obj):
	#	return ("%s" % (obj.iddepartamento)).upper()

	#upper_case_iddepartamento.short_description = 'Departamento' 

	#def nombreMunicipio_upper(self):
		#return("%s" % (self.nombreMunicipio)).upper()

	#nombreMunicipio_upper.short_description = 'Municipio grandeeeeeeeee'

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ('nombreMunicipio', 'iddepartamento')
	#list_filter = ('')
	#list_instanaces = True
	search_fields = ['ForeignKey_related_iddepartamento']


		

class TipoCentro(models.Model):
	nombreTipoCentro = models.CharField(max_length=45)

class TipoCentroAdmin(admin.ModelAdmin):
	list_display = ('nombreTipoCentro',)


class Resenia(models.Model):
	descripcion = models.TextField()
	propietario = models.CharField(max_length=30)

class ReseniaAdmin(admin.ModelAdmin):
	list_display = ('descripcion', 'propietario')
	fields = ('propietario', 'descripcion')

class Servicio(models.Model):
	nombreServicio = models.CharField(max_length =45)

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('nombreServicio',)

class Asignacion(models.Model):
	idservicio = models.ForeignKey('Servicio')
	idperfil = models.ForeignKey('Perfil')		

class AsignacionAdmin(admin.ModelAdmin):
	list_display = ('idservicio', 'idperfil')
		

class Perfil(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length = 50)
	telefono = models.DecimalField(max_digits = 8, decimal_places = 0)
	correo = models.EmailField(max_length = 75)
	mision = models.TextField()
	vision = models.TextField()
	usuario = models.CharField(max_length=20)
	contrasenia = models.CharField(max_length=15)
	correoAdministrador = models.EmailField(max_length = 75)
	idmunicipio = models.ForeignKey('Municipio')
	idtipocentro= models.ForeignKey('TipoCentro')
	idresenia = models.ForeignKey('Resenia')
	idevento = models.ForeignKey('Evento')

class PerfilAdmin(admin.ModelAdmin):
	list_display = ('nombre','direccion','telefono','idmunicipio')
	list_filter = ('usuario',)
	#filter_horizontal = ('Municipio',)

class Evento(models.Model):
	descripcionEvento = models.TextField()
	fechaEvento = models.DateTimeField()

class EventoAdmin(admin.ModelAdmin):
	list_display = ('descripcionEvento','fechaEvento')

class Promociones(models.Model):
	descripcionPromociones = models.TextField()
	fechainicio = models.DateTimeField()
	fechafin = models.DateTimeField()
	def descripcionPromociones_upper(self):
		return ("%s" % (self.descripcionPromociones)).upper()

	descripcionPromociones_upper.short_description = 'Promociones'


class PromocionesAdmin(admin.ModelAdmin):
	list_display = ('descripcionPromociones', 'fechainicio', 'fechafin')
		


admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(TipoCentro, TipoCentroAdmin)
admin.site.register(Promociones, PromocionesAdmin)
admin.site.register(Resenia, ReseniaAdmin)
admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Evento, EventoAdmin)