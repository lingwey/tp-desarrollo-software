from django import forms
from .models import Usuario, Cliente, ChoferParticular, ChoferEmpresa

class UsuarioForm(forms.ModelForm):
    # Para ocultar la contraseñas
    password = forms.CharField(widget=forms.PasswordInput())  
    class Meta:
        model = Usuario
        fields = ['nombreUsuario','email', 'password', 'tipo', 'telefono', 'direccion']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['preferencia_contacto', 'dni']

class ChoferParticularForm(forms.ModelForm):
    class Meta:
        model = ChoferParticular
        fields = ['dni', 'licencia', 'vehiculo', 'seguro_url', 'aprobado']

class ChoferEmpresaForm(forms.ModelForm):
    class Meta:
        model = ChoferEmpresa
        fields = ['cuit', 'razon_social', 'seguro_url', 'aprobado']
