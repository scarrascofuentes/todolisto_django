from django.contrib import admin
from .models import Tarea, TipoTarea, EstadoTarea

# Register your models here.
#Esto carga los modelos al panel de administración de django
admin.site.register(Tarea)
admin.site.register(TipoTarea)
admin.site.register(EstadoTarea)
