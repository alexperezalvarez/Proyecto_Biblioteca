from django.shortcuts import redirect, render
from django.core.exceptions import *
from .forms import *
from .models import *

# Create your views here.
def Home(request):
  return render(request, 'index.html')

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