from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .forms import LoginForm, ProductoForm
from .models import Producto, Categoria
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

@login_required
def index(request):
    return render(request, "core/index.html")

@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Obtener los valores de los filtros enviados por el formulario
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    categorias_seleccionadas = request.GET.getlist('categoria')

    # Filtrar por precio mínimo y máximo
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    # Filtrar por categorías seleccionadas
    if categorias_seleccionadas:
        productos = productos.filter(categoria__in=categorias_seleccionadas)

    return render(request, 'core/listado_productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def nuevo_producto(request):
    data = {"form": ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, "core/nuevo_producto.html", data)


@login_required
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
@login_required
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
@login_required
def agregar(request):
    return render(request, 'core/agregar.html')

@login_required
def buscar_producto(request):
    search_input = request.GET.get('search_input', '').lower()
    # Filtrar los productos que coincidan con el criterio de búsqueda
    filtered_products = Producto.objects.filter(nombre__icontains=search_input)

    context = {
        'products': filtered_products,
        'search_input': search_input,
    }
    return render(request, 'core/buscar_producto.html', context)
@login_required
def ventas(request):
    return render(request, 'core/ventas.html')
@login_required
def buscar_producto_ajax(request):
    search_input = request.GET.get('search_input', '').lower()
    # Filtrar los productos que coincidan con el criterio de búsqueda
    filtered_products = Producto.objects.filter(nombre__icontains=search_input)

    # Preparar los resultados para enviar como respuesta JSON
    results = [
        {
            'nombre': product.nombre,
            'descripcion': product.descripcion,
            'precio': str(product.precio),
            'categoria': product.categoria.nombre,
        }
        for product in filtered_products
    ]
    return JsonResponse(results, safe=False)
def generar_boleta(request):
    # Obtener información para la boleta desde la base de datos.
    # Por ejemplo, aquí se asume que tienes una lista de IDs de productos 'shoppingCart' y
    # que cada elemento del carrito es un objeto Producto con los campos 'nombre', 'precio', 'descuento'.
    shopping_cart_ids = [1, 2, 3]  # IDs de los productos seleccionados en el carrito
    shoppingCart = [get_object_or_404(Producto, id=product_id) for product_id in shopping_cart_ids]

    # Calcular el total a pagar
    total_amount = sum(product.precio * (1 - product.descuento / 100) for product in shoppingCart)

    # Generar el PDF de la boleta usando reportlab.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, 'BOLETA DE VENTA')

    y_position = 700
    for product in shoppingCart:
        p.drawString(100, y_position, f"{product.nombre} - Precio: ${product.precio} - Descuento: {product.descuento}%")
        y_position -= 20

    p.drawString(100, y_position, f'Total a Pagar: ${total_amount:.2f}')

    p.save()
    return response
@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if 'carrito' not in request.session:
        request.session['carrito'] = []

    request.session['carrito'].append(producto_id)
    request.session.modified = True

    return redirect('listado_productos')
def modificar(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Obtener los valores de los filtros enviados por el formulario
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    categorias_seleccionadas = request.GET.getlist('categoria')

    # Filtrar por precio mínimo y máximo
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    # Filtrar por categorías seleccionadas
    if categorias_seleccionadas:
        productos = productos.filter(categoria__in=categorias_seleccionadas)

    return render(request, 'core/listado_productos.html', {'productos': productos, 'categorias': categorias})
# firebase login
# firebase init
# firebase deploy
