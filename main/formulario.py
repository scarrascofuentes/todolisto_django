from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import date
from .models import Tarea
from django.utils.translation import ugettext_lazy as _



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Username',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
		}
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user





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
