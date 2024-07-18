from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Producto, Inventario, Venta
from .serializers import ProductoSerializer, InventarioSerializer, VentaSerializer

# genero las vistas de mi app inventario utilizando el framework Django Rest Framework.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


