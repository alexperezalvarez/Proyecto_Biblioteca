from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.usuarios'  # ✅ Agrega "app." antes del nombre
