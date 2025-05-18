from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import perfil_usuario, home, logout_usuario, login_usuario, registro_usuario

urlpatterns = [
    # usa la autenticación integrada de django y habilita el uso de log in, log out, cambio de contraseña y restablecer contraseña con el email 
    path("accounts/", include("django.contrib.auth.urls")),  
    path('', home, name='home' ),
    path('logout/', logout_usuario, name='logout'),
    path('login/', login_usuario, name='login_usuario'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('/registrarse', registro_usuario, name='registro_usuario')
]
