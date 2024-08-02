from rest_framework import viewsets
from .models import Producto, Inventario, Venta
from .serializers import ProductoSerializer, InventarioSerializer, VentaSerializer

# Generate the views for the inventario app using Django Rest Framework.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
