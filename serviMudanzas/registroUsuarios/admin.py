from django.contrib import admin
from .models import Usuario, Cliente, ChoferParticular, ChoferEmpresa

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombreUsuario','email', 'tipo', 'telefono', 'fecha_registro')
    search_fields = ('nombreUsuario','email', 'tipo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dni', 'preferencia_contacto')
    search_fields = ('usuario__email', 'dni')

@admin.register(ChoferParticular)
class ChoferParticularAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dni', 'licencia', 'aprobado')
    search_fields = ('usuario__email', 'dni')

@admin.register(ChoferEmpresa)
class ChoferEmpresaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cuit', 'razon_social', 'aprobado')
    search_fields = ('usuario__email', 'cuit')
