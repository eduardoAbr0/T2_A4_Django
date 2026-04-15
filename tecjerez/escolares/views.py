from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

#--ALTAS
#--
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno agregado con exito"

    def get_success_url(self):
        return reverse('listar')

#--BAJAS
#--
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = "__all__"

    def get_success_url(self):
        success_mesage = "Alumno eliminado correctamente"
        messages.success(self.request, success_mesage)
        return reverse('listar')
    
    
#--CAMBIOS
#--
class ModificarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno modificado correctamete"

    def get_success_url(self):
        return reverse('listar')
    
#--CONSULTAS
#--
class DetalleAlumno(DetailView):
    model = Alumno

class ListadoAlumno(ListView):
    model = Alumno