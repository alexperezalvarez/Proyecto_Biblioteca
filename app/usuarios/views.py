from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.utils.decorators import *
from django.views.decorators.cache import *
from django.views.decorators.csrf import *
from app.usuarios.forms import FomularioLogin
from django.contrib.auth import *

class Login(FormView):
  template_name = 'login.html'
  form_class = FomularioLogin
  success_url = reverse_lazy('index')

  @method_decorator(csrf_protect)
  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return HttpResponseRedirect(self.get_success_url())
    else:
      return super(Login,self).dispatch(request,*args,**kwargs)
    
  def form_valid(self, form):
    login(self.request,form.get_user())
    return super(Login,self).form_valid(form)