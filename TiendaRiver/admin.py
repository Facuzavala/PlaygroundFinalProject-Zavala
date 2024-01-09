from django.contrib import admin
from TiendaRiver.models import Cliente, Producto, ModoPago, Avatar
from TiendaRiver import models

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    list_filter = ("apellido", "email")
    search_fields = ("apellido", "email")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("articulo", "talle", "precio")
    list_filter = ("articulo", "precio")
    search_fields = ("articulo", "precio")

@admin.register(ModoPago)
class ModoPagoAdmin(admin.ModelAdmin):
    list_display = ("metodopago", "total")
    list_filter = ("metodopago", "total")
    search_fields = ("metodopago", "total")

admin.site.register(models.Avatar)






