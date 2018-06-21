from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Tarea, TipoTarea, EstadoTarea
from .formulario import Registro, TareaForm

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
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.tipo = TipoTarea.objects.get(id=(request.POST.get('tipo')))
        tarea.estado = EstadoTarea.objects.get(id=(request.POST.get('estado')))
        tarea.usuario = request.user
        tarea.save()
    tareas = Tarea.objects.filter(usuario=request.user)
    tipos = TipoTarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos})

class EliminarTarea(DeleteView):
	model = Tarea
	template_name = 'eliminarTarea.html'
	success_url = reverse_lazy('tareas')

class EditarTarea(UpdateView):
	model = Tarea
	form_class = TareaForm
	template_name = 'formTarea.html'
	success_url = reverse_lazy('tareas')

class DetalleTarea(DetailView):
	model = Tarea
	template_name = 'detalleTarea.html'
