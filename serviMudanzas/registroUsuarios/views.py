from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import EmailLoginForm
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = "registroUsuarios/login.html"

@login_required
def perfil_usuario(request):
    return render(request, 'accounts/perfil.html', {"usuario":request.user})