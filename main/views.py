from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
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

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
