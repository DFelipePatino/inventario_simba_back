from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Producto, Inventario, Venta
from .serializers import ProductoSerializer, InventarioSerializer, VentaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

def delete_product_view(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    product.delete_product()
    return HttpResponse("Product deleted successfully.")
