from django.contrib import admin
from .models import Producto, Inventario, Venta

admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Venta)