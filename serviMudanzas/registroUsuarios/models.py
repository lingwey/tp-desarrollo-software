from django.db import models

class Usuario(models.Model):
    #base para los diferentes tipos de usuarios
    CLIENTE = 'cliente'
    CHOFER_PARTICULAR = 'chofer_particular'
    CHOFER_EMPRESA = 'chofer_empresa'

    TIPO_USUARIO_CHOICES = [
        (CLIENTE, 'Cliente'),
        (CHOFER_PARTICULAR, 'Chofer Particular'),
        (CHOFER_EMPRESA, 'Chofer Empresa'),
    ]
    nombreUsuario = models.CharField(max_length=40, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    telefono = models.CharField(max_length=20, unique=True, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} ({self.tipo})"

#eredan de la clase usurios y cada uno lo modifica segun su tipo de usuario
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(max_length=20)
    preferencia_contacto = models.CharField(max_length=50, default='whatsapp')

class ChoferParticular(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(max_length=20)
    licencia = models.CharField(max_length=50)
    #vehiculo = models.OneToOneField('Vehiculo', on_delete=models.SET_NULL, null=True, unique=True)
    seguro_url = models.CharField(max_length=255, null=True, blank=True)
    aprobado = models.BooleanField(default=False)

class ChoferEmpresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cuit = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=100)
    seguro_url = models.CharField(max_length=255, null=True, blank=True)
    aprobado = models.BooleanField(default=False)
