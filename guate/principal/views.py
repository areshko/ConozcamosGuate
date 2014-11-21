from django.template import loader, Context
from django.http import HttpResponse
from principal.models import Evento
from principal.models import Departamento
from principal.models import Municipio

def archive(request):
	evento1 = Evento.objects.all()
	mi_template = loader.get_template("archive.html")
	mi_contexto = Context({'evento1':evento1})
	return HttpResponse(mi_template.render(mi_contexto))
# Create your views here.

def archiveDepartamentos(request):
	departamento1 = Departamento.objects.all()
	mi_template = loader.get_template("archiveDepartamentos.html")
	mi_contexto = Context({'departamento1':departamento1})
	return HttpResponse(mi_template.render(mi_contexto))

def archiveMunicipios(request):
	departamento1 = Departamento.objects.all()
	municipio1 = Municipio.objects.all()
	mi_template = loader.get_template("archiveMunicipios.html")
	mi_contexto = Context({'municipio1':municipio1})
	return HttpResponse(mi_template.render(mi_contexto))