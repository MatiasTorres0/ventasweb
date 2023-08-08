from django import forms
from django.forms import ModelForm
from .models import Producto, Reparto, Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_barras', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen', 'unidad_medida', 'tamano', 'oferta', 'descuento']


class CustomUserForm(UserCreationForm):
    class Meta:

        model = User 
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']



class RepartoForm(forms.ModelForm):
    class Meta:
        model = Reparto
        fields = ['fecha', 'region', 'ciudad', 'comuna', 'direccion', 'persona_recibe', 'numero_contacto']


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen']