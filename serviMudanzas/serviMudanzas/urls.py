from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #hace el manejo de autenticación con django
    path('accounts/', include('django.contrib.auth.urls')), 
    #es el URLs de la app registroUsuarios 
    path('usuarios/', include('registroUsuarios.urls')),
]
