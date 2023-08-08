from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, login, index, listado_productos, nuevo_producto, modificar_producto, eliminar_producto, agregar, crear, soporte
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
    path('cargar-productos/', views.cargar_productos_desde_excel, name='cargar_productos'),
    path('actualizar-informacion-desde-excel/', views.actualizar_informacion_desde_excel, name='actualizar_informacion_desde_excel'),
    path('cargar-categorias/', views.cargar_categorias_desde_excel, name='cargar_categorias'),
    path('cargar-unidades/', views.cargar_unidades_desde_excel, name='cargar_unidades'),
    path('cargar-tamanos/', views.cargar_tamanos_desde_excel, name='cargar_tamanos'),
    path('escanear_codigo_barras/', views.escanear_codigo_barras, name='escanear_codigo_barras'),
    path('crear/', crear, name="crear"),
    path('soporte/', soporte, name="soporte"),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('responder_ticket/<int:ticket_id>/', views.responder_ticket, name='responder_ticket'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('registrar/', views.registro_usuario, name="registro_usuario"),
    path('reparto/', views.reparto_list, name='reparto_list'),
    path('reparto/<int:pk>/', views.reparto_detail, name='reparto_detail'),
    path('reparto/crear/', views.reparto_create, name='reparto_create'),
    path('crearnoticia/', views.crear_noticia, name='crear_noticia'),
    path('lista/', views.lista_noticias, name='lista_noticias'),
    path('creararticulo/', views.creararticulo, name="creararticulo"),
    path('detalle_noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
]