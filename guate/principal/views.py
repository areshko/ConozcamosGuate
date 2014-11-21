from django.template import loader, Context
from django.http import HttpResponse
from principal.models import Evento
from principal.models import Departamento
from principal.models import Municipio
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from principal.forms import FormDepartamento
from principal.forms import *


def archive(request):
	evento1 = Evento.objects.all()
	return render_to_response('archive.html',{'evento1':evento1})
	#mi_template = loader.get_template("archive.html")
	#mi_contexto = Context({'evento1':evento1})
	#return HttpResponse(mi_template.render(mi_contexto))
# Create your views here.

def archiveDepartamentos(request):
	departamento1 = Departamento.objects.all()
	return render_to_response('archiveDepartamentos.html',{'departamento1':departamento1})
	#mi_template = loader.get_template("archiveDepartamentos.html")
	#mi_contexto = Context({'departamento1':departamento1})
	#return HttpResponse(mi_template.render(mi_contexto))

def archiveMunicipios(request):
	municipio1 = Municipio.objects.all()
	return render_to_response('archiveMunicipios.html',{'municipio1':municipio1})
	#mi_template = loader.get_template("archiveMunicipios.html")
	#mi_contexto = Context({'municipio1':municipio1})
	#return HttpResponse(mi_template.render(mi_contexto))

def formularioDepartamento(request):
	if request.method=="POST":
		formularioDepartamento = FormDepartamento(request.POST)
		if formularioDepartamento.is_valid():
			formularioDepartamento.save()
			return HttpResponseRedirect("/departamentos")
	else:
		formularioDepartamento=FormDepartamento()
	return render(request, 'agregaraDepartamento.html', {'formulario':formularioDepartamento})

def formularioEvento(request):
	if request.method=="POST":
		formularioEvento = FormEvento(request.POST)
		if formularioEvento.is_valid():
			formularioEvento.save()
	else:
		formularioEvento=FormEvento()
	return render(request, 'agregarEvento.html', {'formulario':formularioEvento})

def formularioMunicipio(request):
	if request.method=="POST":
		formularioMunicipio = FormMunicipio(request.POST)
		if formularioMunicipio.is_valid():
			formularioMunicipio.save()
			return HttpResponseRedirect("/municipios")
	else:
		formularioMunicipio=FormMunicipio()
	return render(request, 'agregarMunicipio.html', {'formulario':formularioMunicipio})
