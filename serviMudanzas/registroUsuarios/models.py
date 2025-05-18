from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        extra_fields.setdefault("is_active", True)
        usuario = self.model(email=self.normalize_email(email), **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    CLIENTE = 'cliente'
    CHOFER_PARTICULAR = 'chofer_particular'
    CHOFER_EMPRESA = 'chofer_empresa'

    TIPO_USUARIO_CHOICES = [
        (CLIENTE, 'Cliente'),
        (CHOFER_PARTICULAR, 'Chofer Particular'),
        (CHOFER_EMPRESA, 'Chofer Empresa'),
    ]

    email = models.EmailField(unique=True)
    nombreUsuario = models.CharField(max_length=40, null=True, blank=True, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    telefono = models.CharField(max_length=20, unique=True, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombreUsuario"]

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.email} ({self.tipo})"


#eredan de la clase usurios y cada uno lo modifica segun su tipo de usuario
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(max_length=20)
    preferencia_contacto = models.CharField(max_length=50, default='whatsapp')



class ChoferEmpresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cuit = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=100)
    seguro_url = models.CharField(max_length=255, null=True, blank=True)
    aprobado = models.BooleanField(default=False)

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=50)
    patente = models.CharField(max_length=20, unique=True)
    capacidad_kg = models.FloatField()
    tiene_acoplado = models.BooleanField(default=False)
    notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.patente}"
    
class ChoferParticular(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(max_length=20)
    licencia = models.CharField(max_length=50)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    seguro_url = models.CharField(max_length=255, null=True, blank=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.email} - {self.vehiculo}"