from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Tarea
from .formulario import Registro

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = Registro
    success_url = reverse_lazy('login')

@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, "tareas.html", { 'tareas' : tareas})

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo_tarea')
        tarea.descripcion = request.POST.get('descripcion_tarea')
        tarea.usuario = request.user
        tarea.save()
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, "tareas.html", { 'tareas' : tareas})

class EliminarTarea(DeleteView):
	model = Tarea
	template_name = 'eliminarTarea.html'
	success_url = reverse_lazy('tareas')
