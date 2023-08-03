from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, login, index, listado_productos, nuevo_producto, modificar_producto, eliminar_producto, agregar
from . import views
urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('listado_productos/', listado_productos, name="listado_productos"),
    path('nuevo_producto/', nuevo_producto, name="nuevo_producto"),
    path('modificar_producto/<int:id>/', views.modificar_producto, name="modificar_producto"),
    path('eliminar_producto/', eliminar_producto, name="eliminar_producto"),
    path('agregar/', agregar, name="agregar"),
    path('buscar-producto/', views.buscar_producto, name="buscar_producto"),
    path('ventas/', views.ventas, name="ventas"),
    path('buscar-producto-ajax/', views.buscar_producto_ajax, name="buscar_producto_ajax"),
    path('generar-boleta/', views.generar_boleta, name="generar_boleta"),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name="agregar_al_carrito"),
    path('modificar', views.modificar, name = "modificar"),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
    path('carrito/', views.carrito_ventas, name="carrito_ventas"),
    path('realizar_pago/', views.realizar_pago, name='realizar_pago'),
    path('chat/', views.chat_room, name='chat-room'),
    path('send_message/', views.send_message, name='send-message'),
    path('get_messages/', views.get_messages, name='get-messages'),
    path('nueva-conversacion/', views.nueva_conversacion, name='nueva_conversacion'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('worker_chat/', LoginView.as_view(template_name='worker_chat.html'), name='worker-chat'),
]