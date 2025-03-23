from django import forms
from .models import *

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
    labels = {
      'nombre': 'Nombre del autor',
      'apellidos':'apellidos del autor',
      'descripcion':'Descripcion del autor'
    }
    widgets = {
      'nombre' : forms.TextInput(
        attrs = {
          'class' : 'form-control',
          'placeholder': 'Nombre'
        }
      ),
      'apellidos' : forms.TextInput(
        attrs = {
          'class' : 'form-control',
          'placeholder': 'Apellidos'
        }
      ), 'descripcion' : forms.TextInput(
        attrs = {
          'class' : 'form-control',
          'placeholder': 'Descripción'
        }
      )
    }