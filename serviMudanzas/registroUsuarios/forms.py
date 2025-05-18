from django import forms
from .models import Usuario, Cliente, ChoferParticular, ChoferEmpresa, Vehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class RegistroUsuarioForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, label="Tipo de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

    class Meta:
        model = Usuario
        fields = ["nombreUsuario", "email", "password", "tipo_usuario", "telefono", "direccion"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # Encripta la contraseña correctamente
        usuario.set_password(self.cleaned_data["password"])  
        if commit:
            usuario.save()
        return usuario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["dni", "preferencia_contacto"]
        widgets = {
            "dni": forms.TextInput(attrs={"id": "id_dni_cliente"}),  # ID único
        }

class ChoferParticularForm(forms.ModelForm):
    vehiculo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ejemplo: Camioneta, Furgón"}), required=True, label="Tipo de vehículo")
    class Meta:
        model = ChoferParticular
        fields = ["dni", "licencia", "vehiculo", "seguro_url"]
        widgets = {
            "dni": forms.TextInput(attrs={"id": "id_dni_chofer"}),
            "seguro_url": forms.TextInput(attrs={"id": "id_seguro_chofer"}),
        }

class ChoferEmpresaForm(forms.ModelForm):
    class Meta:
        model = ChoferEmpresa
        fields = ["cuit", "razon_social", "seguro_url"]
        widgets = {
            "cuit": forms.TextInput(attrs={"id": "id_cuit_empresa"}),
            "razon_social": forms.TextInput(attrs={"id": "id_razon_empresa"}),
            "seguro_url": forms.TextInput(attrs={"id": "id_seguro_empresa"}),
        }

# Formulario de login con email y contraseña
class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
