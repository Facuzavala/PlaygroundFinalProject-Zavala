from django.urls import path
from TiendaRiver import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("inicio", views.inicio, name="inicio"),
    path("clientes/", views.clientes, name= "cliente"),
    path("productos/", views.productos, name="producto"),
    path("modopago/", views.modopagos, name="modo_pago"),
    path("clienteFormulario/", views.clientes_formulario, name="cliente_formulario"),
    path("productoFormulario/", views.productos_formulario, name="producto_formulario"),
    path("modopagoFormulario/", views.modopagos_formulario, name="modopago_formulario"),
    path("buscarCliente/", views.buscar_cliente, name="buscar clientes"),
    path("buscar/", views.buscar, name = "buscar"),
    path("leerModoPago/", views.leer_modopagos, name="Leermodopago"),
    path('eliminarModoPago/<modopago_metodopago>/', views.eliminar_modopago, name="EliminarModoPago"),
    path('editarModoPago/<modopago_metodopago>/', views.editar_modopago, name="EditarModoPago"),

    path('clientes/lista', views.ClienteListView.as_view(), name = "ListaClientes"),
    path('clientes/nuevo', views.ClienteCreateView.as_view(), name = "NuevoCliente"),
    path('clientes/<pk>', views.ClienteDetailView.as_view(), name = "DetalleCliente"),
    path('clientes/<pk>/editar', views.ClienteUpdateView.as_view(), name = "EditarCliente"),
    path('clientes/<pk>/borrar', views.ClienteDeleteView.as_view(), name = "BorrarCliente"),

    path('productos/lista', views.ProductoListView.as_view(), name = "ListaProductos"),
    path('productos/nuevo', views.ProductoCreateView.as_view(), name = "NuevoProducto"),
    path('productos/<pk>', views.ProductoDetailView.as_view(), name = "DetalleProducto"),
    path('productos/<pk>/editar', views.ProductoUpdateView.as_view(), name = "EditarProducto"),
    path('productos/<pk>/borrar', views.ProductoDeleteView.as_view(), name = "BorrarProducto"),

    path('login/', views.user_login, name= "user_login"),
    path('register/', views.user_register, name= "user_register"),
    path('logout/', views.user_logout, name ="user_logout"),
    path('editarPerfil/', views.editarPerfil, name ="EditarPerfil"),
    path('cambiarContrasenia/', views.CambiarContrasenia.as_view(), name ="CambiarContrasenia"),

    path('about/', views.about, name='acercademi'),

] 

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)