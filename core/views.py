from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, ProductoForm
from .models import Producto
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "core/home.html")


def login(request):
    return render(request, "core/login.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la página deseada después del inicio de sesión
                return redirect("pagina_despues_login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    # Redirige a la página deseada después del cierre de sesión
    return redirect("pagina_despues_logout")


def index(request):
    return render(request, "core/index.html")


def listado_productos(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, "core/listado_productos.html", data)


def nuevo_producto(request):
    data = {"form": ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, "core/nuevo_producto.html", data)



def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' :ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El producto fue modificado Correctamente")
            return redirect("listado_productos")
    return render(request, 'core/modificar_producto.html', data)

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

# firebase login
# firebase init
# firebase deploy
