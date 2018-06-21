from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoTarea (models.Model):
    nombre = models.CharField(max_length = 255)

    def __str__(self):
	    return '{}'.format(self.nombre)

class EstadoTarea (models.Model):
    nombre = models.CharField(max_length = 255)

    def __str__(self):
	    return '{}'.format(self.nombre)


class Tarea (models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    tipo = models.ForeignKey(TipoTarea, on_delete = models.CASCADE)
    estado = models.ForeignKey(EstadoTarea, on_delete = models.CASCADE)
