from django.shortcuts import redirect, render
from django.core.exceptions import *
from .forms import *
from .models import *
from django.views.generic import *
# Create your views here.

"""
1- dispctch(): Valida la peticion y elige que metodo HTTP se utilizo para la solicitud
2- http_method_not_allowed(): Retorna un error cuando se utiliza un metodo HTTP no soportado o definido
3- options()
"""


class Inicio(TemplateView):
   template_name = 'index.html'

def crearAutor(request):
  if request.method == 'POST':
    autor_form = AutorForm(request.POST)
    if autor_form.is_valid():
      autor_form.save()
      return redirect('index')
  else:
    autor_form = AutorForm()
    print(autor_form)
  return render(request, 'libro/crear_autor.html',{'autor_form': autor_form})

def listarAutor(request):
  autores = Autor.objects.filter(estado = True)
  return render(request, 'libro/listar_autor.html', {'autores': autores})

def editarAutor(request, id):
    try:
        autor = Autor.objects.get(id=id)  # Obtener el autor
        error = None  # Inicializar error

        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')  # Redirigir solo si se guarda el formulario

        # Si hay errores o es un método GET, renderiza el formulario
        return render(request, 'lirbo/crear_autor.html', {'autor_form': autor_form, 'error': error})

    except ObjectDoesNotExist as e:
        error = f"Error: {e}"
        return render(request, 'libro/crear_autor.html', {'autor_form': None, 'error': error})

def eliminarAutor(request, id):
   autor = Autor.objects.get(id = id)
   if request.method == 'POST':
      autor.estado=False
      autor.save()
      return redirect('libro/listar_autor') 
   return render(request, 'libro/eliminar_autor.html',{'autor':autor})