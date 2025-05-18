from django.contrib.auth import get_user_model

Usuario = get_user_model()

class EmailAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            usuario = Usuario.objects.get(email=username)
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
