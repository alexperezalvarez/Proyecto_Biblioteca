"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from app.views import ActualizarAutor, CrearAutor, EliminarAutor, Inicio, ListadoAutor, ServiciosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('app.urls'))),
    path('', login_required(Inicio.as_view()), name='index'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('crear_autor/',login_required( CrearAutor.as_view()), name='crear_autor'),
    path('listar_autor/',login_required(ListadoAutor.as_view()), name='listar_autor'),
    path('editar_autor/<int:pk>',login_required(ActualizarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),
    path('servicios/',login_required(ServiciosView.as_view()), name='servicios'),
  
]

