from django.urls import path
from .views import home, login, index, listado_productos, nuevo_producto, modificar_producto, eliminar_producto
from . import views
urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('listado_productos/', listado_productos, name="listado_productos"),
    path('nuevo_producto/', nuevo_producto, name="nuevo_producto"),
    path('modificar_producto/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/', eliminar_producto, name="eliminar_producto"),
]