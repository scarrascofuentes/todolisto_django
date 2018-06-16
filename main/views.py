from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def tareas(request):
    return render(request, "tareas.html")
