from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tarea

# Create your views here.
@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas})

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo_tarea')
        tarea.descripcion = request.POST.get('descripcion_tarea')
        #tarea.usuario = request.user
        tarea.save()
    tareas = Tarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas})
