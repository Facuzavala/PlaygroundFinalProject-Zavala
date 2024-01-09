from django.shortcuts import render
from django.http import HttpResponse
from TiendaRiver.models import Cliente, Producto, ModoPago
from TiendaRiver.forms import ClienteFormulario, ProductoFormulario, ModoPagoFormulario, UserCreationFormCustom, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

#Create your views here.

def inicio(request):
    return render(request, "TiendaRiver/inicio.html")


def clientes(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre = informacion["nombre"],apellido = informacion["apellido"], email = informacion["email"])
            cliente.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "TiendaRiver/cliente.html", {"mi_formulario": mi_formulario})

def productos(request):
    if request.method == "POST":
        mi_formulario = ProductoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(articulo = informacion["articulo"],talle = informacion["talle"], precio= informacion["precio"])
            producto.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ProductoFormulario()
        return render(request, "TiendaRiver/producto.html", {"mi_formulario": mi_formulario})

def modopagos(request):
    if request.method == "POST":
        mi_formulario = ModoPagoFormulario(request.POST, request.FILES)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            modopagos = ModoPago(metodopago = informacion["metodopago"],total = informacion["total"])
            modopagos.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ModoPagoFormulario()
        return render(request, "TiendaRiver/modopago.html", {"mi_formulario": mi_formulario})


def clientes_formulario(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre = informacion["nombre"],apellido = informacion["apellido"], email = informacion["email"])
            cliente.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "TiendaRiver/cliente_formulario.html", {"mi_formulario": mi_formulario})

def productos_formulario(request):
    if request.method == "POST":
        mi_formulario = ProductoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(articulo = informacion["articulo"],talle = informacion["talle"], precio= informacion["precio"])
            producto.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ProductoFormulario()
        return render(request, "TiendaRiver/producto_formulario.html", {"mi_formulario": mi_formulario})

def modopagos_formulario(request):
    if request.method == "POST":
        mi_formulario = ModoPagoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            modopago = ModoPago(metodopago = informacion["metodopago"],total = informacion["total"])
            modopago.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ModoPagoFormulario()
        return render(request, "TiendaRiver/modopago_formulario.html", {"mi_formulario": mi_formulario})

@login_required    
def buscar_cliente(request):
    return render(request, "TiendaRiver/buscar_cliente.html")

def buscar(request):
    apellido = request.GET.get("apellido", "")
    if apellido:
        resultados = Cliente.objects.filter(apellido__icontains=apellido)
        return render(request, "TiendaRiver/busquedacliente.html", {"apellido": apellido, "resultados": resultados})
    else:
        respuesta = "No se ha ingresado ningun dato, intente nuevamente."
        return HttpResponse(respuesta)
    
#Leer Modos de Pago
    
def leer_modopagos(request):
    modopagos = ModoPago.objects.all()
    contexto = {"ModoPago" : modopagos}

    return render(request, 'TiendaRiver/leerModoPago.html', contexto)

#Eliminar Modos de Pago

def eliminar_modopago(request, modopago_metodopago):
    modopago = ModoPago.objects.get(metodopago= modopago_metodopago)
    modopago.delete()

    modopagos = ModoPago.objects.all()
    contexto = {"ModoPago" : modopagos}
    return render(request, 'TiendaRiver/leerModoPago.html', contexto)

#Editar Modos de Pago

def editar_modopago(request, modopago_metodopago):
    modopago = ModoPago.objects.get(metodopago = modopago_metodopago)
    if request.method == "POST":
        mi_formulario = ModoPagoFormulario(request.POST, request.FILES)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            modopago.metodopago = informacion["metodopago"]
            modopago.total = informacion["total"]
            

            modopago.save()
            return render(request, "TiendaRiver/inicio.html")
    else:
        mi_formulario = ModoPagoFormulario(initial={"metodopago": modopago.metodopago,
                                                "total": modopago.total})
            
    return render(request, "TiendaRiver/editarmodopago.html", {"mi_formulario": mi_formulario, "modopago_metodopago": modopago_metodopago})
    

class ClienteListView(ListView):
    model = Cliente
    context_object_name = "clientes"
    template_name = "TiendaRiver/clientes_lista.html"

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "TiendaRiver/clientes_detalle.html"


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "TiendaRiver/clientes_crear.html"
    success_url = reverse_lazy("ListaClientes")
    fields = ["nombre", "apellido", 'email', 'imagen']

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "TiendaRiver/clientes_editar.html"
    success_url = reverse_lazy("ListaClientes")
    fields = ["nombre", "apellido", 'email', 'imagen']

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "TiendaRiver/clientes_borrar.html"
    success_url = reverse_lazy("ListaClientes")


class ProductoListView(ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "TiendaRiver/productos_lista.html"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "TiendaRiver/productos_detalle.html"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "TiendaRiver/productos_crear.html"
    success_url = reverse_lazy("ListaProductos")
    fields = ["articulo", "talle", 'precio']

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "TiendaRiver/productos_editar.html"
    success_url = reverse_lazy("ListaProductos")
    fields = ["articulo", "talle", 'precio']

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "TiendaRiver/productos_borrar.html"
    success_url = reverse_lazy("ListaProductos")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"TiendaRiver/inicio.html")
        else:
            return render(request, "TiendaRiver/login.html", {"error": "Nombre de usuario o contraseña incorrectos."})
    return render(request, "TiendaRiver/login.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request, "TiendaRiver/inicio.html")

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "TiendaRiver/login.html")
    else:
        form = UserCreationForm()
    return render(request, "TiendaRiver/register.html", {"form": form})

def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get("imagen")
                usuario.avatar.save()
            mi_formulario.save()
            return render(request, "TiendaRiver/inicio.html")
    else:       
        mi_formulario = UserEditForm(initial={"imagen": usuario.avatar.imagen}, instance= request.user)
    return render(request, "TiendaRiver/editarPerfil.html", {"mi_formulario": mi_formulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "TiendaRiver/cambiar_clave.html"
    success_url = reverse_lazy("EditarPerfil")

def about(request):
    return render(request, 'TiendaRiver/acercademi.html', {})

