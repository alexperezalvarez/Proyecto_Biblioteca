from django.contrib.auth.forms import *

class FomularioLogin(AuthenticationForm):
  def __init__(self, request = ..., *args, **kwargs):
    super(FomularioLogin).__init__(*args, **kwargs)
    self.fields['usermane'].widget.attrs['class'] = 'form_control'
    self.fields['usermane'].widget.attrs['placeholder'] = 'Nombre de Usuario'
    self.fields['password'].widget.attrs['class'] = 'form_control'
    self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
