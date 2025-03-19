from django.shortcuts import redirect, render
from app.forms import *
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
  return render(request, 'crear_autor.html',{'autor_form': autor_form})

def listarAutor(request):
  autores = Autor.objects.all()
  return render(request, 'listar_autor.html', {'autores': autores})