from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import date
from .models import Tarea

class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'usuario',
            'tipo',
            'estado',
            'fechaInicio',
            'fechaTermino',
        ]
        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'usuario': 'Nombre de Usuario',
            'tipo': 'Tipo',
            'estado': 'Estado',
            'fechaInicio': 'Fecha de Inicio',
            'fechaTermino': 'Fecha de Término',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'fechaInicio': forms.DateInput( format='%d/%m/%Y', attrs={'class':'form-control'} ),
            'fechaTermino': forms.DateInput(format='%d/%m/%Y', attrs={'class':'form-control'}),

		}
