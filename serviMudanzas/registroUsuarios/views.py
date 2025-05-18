from django.shortcuts import render, redirect
#from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .forms import EmailLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistroUsuarioForm, ClienteForm, ChoferParticularForm, ChoferEmpresaForm

#class CustomLoginView(LoginView):
#   authentication_form = EmailLoginForm
#   template_name = "registroUsuarios/login.html"

def login_usuario(request):
    if request.method == "POST":
        form = EmailLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(request, username=email, password=password)

            print(f"Autenticando usuario: {usuario}")  # Depuración
            
            if usuario is not None:
                login(request, usuario)
                print("Usuario autenticado. Redirigiendo a perfil.")
                return redirect("perfil_usuario")  # Redirigir correctamente
            else:
                print("Autenticación fallida.")
                return HttpResponse(" Email o contraseña incorrectos.", status=401)

    else:
        form = EmailLoginForm()

    return render(request, "registration/login.html", {"form": form})

@login_required
def perfil_usuario(request):
    if not  request.user.is_authenticated:
        return HttpResponse('inicie secion para ingresar', status=403)
    return render(request, 'registroUsuarios/perfil.html', {"usuario":request.user})

def home(request):
    return render(request,'registroUsuarios/home.html')

def logout_usuario(request):
    logout(request)
    return redirect('home')

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        cliente_form = ClienteForm(request.POST)  
        chofer_form = ChoferParticularForm(request.POST)
        empresa_form = ChoferEmpresaForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["password"])
            # Asignar correctamente el tipo de usuario
            usuario.tipo = form.cleaned_data["tipo_usuario"]  
            usuario.save()
            # Debugging
            print(f"Usuario creado: {usuario.email}, Tipo: {usuario.tipo}")  

            # Crear perfil específico según el tipo de usuario
            if usuario.tipo == "cliente" and cliente_form.is_valid():
                cliente = cliente_form.save(commit=False)
                cliente.usuario = usuario
                cliente.save()

            elif usuario.tipo == "chofer_particular" and chofer_form.is_valid():
                chofer = chofer_form.save(commit=False)
                chofer.usuario = usuario
                chofer.vehiculo = chofer_form.cleaned_data["vehiculo"]
                chofer.save()

            elif usuario.tipo == "chofer_empresa" and empresa_form.is_valid():
                empresa = empresa_form.save(commit=False)
                empresa.usuario = usuario
                empresa.save()
            usuario.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, usuario) 
            return redirect("perfil_usuario")  

        print(" Error al validar el formulario")  

    else:
        form = RegistroUsuarioForm()
        cliente_form = ClienteForm()
        chofer_form = ChoferParticularForm()
        empresa_form = ChoferEmpresaForm()

    return render(request, "registroUsuarios/registro.html", {
        "form": form,
        "cliente_form": cliente_form,
        "chofer_form": chofer_form,
        "empresa_form": empresa_form,
    })
