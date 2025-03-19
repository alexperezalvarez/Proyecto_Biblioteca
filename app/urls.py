from django.urls import path
from .views import *


urlpatterns = [
  path('crear_autor/', crearAutor, name='crear_autor'),
  path('listar_autor/', listarAutor, name='listar_autor')
]