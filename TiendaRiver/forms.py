from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
from django.contrib.auth.models import User

class ClienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.CharField(max_length=50)

class ProductoFormulario(forms.Form):
    articulo = forms.CharField(max_length=50)
    talle = forms.CharField(max_length=10)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class ModoPagoFormulario(forms.Form):
    metodopago= forms.CharField(max_length=50)
    total= forms.DecimalField(max_digits=10, decimal_places=2)

class UserCreationFormCustom(UserCreationForm):
    user = forms.CharField(label="Usuario: ")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña: ", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"] 
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email: ")
    nombre = forms.CharField(label="Nombre: ")
    apellido = forms.CharField(label="Apellido: ")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["email", "apellido", "nombre", "imagen"]

