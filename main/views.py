from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from .models import Tarea, TipoTarea, EstadoTarea
from .formulario import RegistrationForm, TareaForm

# Create your views here.

def root(request):
    return redirect('tareas')


#class RegistroUsuario(CreateView):
#    model = User
#    form_class = Registro
#    template_name = 'registration/signup.html'
#    success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario Creado Satisfactoriamente")
            success_url = reverse_lazy('login')
    else:
        form = UserCreationForm()
        args = {'form': RegistrationForm}
        return render(request, 'registration/signup.html', args)

    return HttpResponseRedirect(reverse_lazy('login'))




@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
@require_GET
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})

@login_required()
@require_POST
def crear_tarea(request):
    tarea = Tarea()
    tarea.titulo = request.POST.get('titulo')
    tarea.descripcion = request.POST.get('descripcion')
    tarea.tipo = TipoTarea.objects.get(id=(request.POST.get('tipo')))
    tarea.estado = EstadoTarea.objects.get(id=(request.POST.get('estado')))
    tarea.usuario = request.user
    tarea.fechaInicio = request.POST.get('fechaInicio')
    tarea.fechaTermino = request.POST.get('fechaTermino')
    tarea.save()
    tareas = Tarea.objects.filter(usuario=request.user)
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})

@login_required()
def calendar_view(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'calendario.html', { 'tareas': tareas})

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
