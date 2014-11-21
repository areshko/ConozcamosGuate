from django.forms import ModelForm
from django import forms
from principal.models import Departamento
from principal.models import Evento
from principal.models import *
from django.contrib.auth.models import User

class  FormDepartamento(ModelForm):
	class Meta:
		model = Departamento

class FormEvento(ModelForm):
	class  Meta:
		model = Evento

class FormMunicipio(ModelForm):
	class Meta:
		model = Municipio