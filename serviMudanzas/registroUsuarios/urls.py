from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import perfil_usuario

urlpatterns = [
    # usa la autenticación integrada de django y habilita el uso de log in, log out, cambio de contraseña y restablecer contraseña con el email 
    path("accounts/", include("django.contrib.auth.urls")),  
    path('perfil/', perfil_usuario, name='perfil_usuario')
]
