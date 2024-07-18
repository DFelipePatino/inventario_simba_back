from rest_framework import serializers
from .models import Producto, Inventario, Venta
import pytz
from django.utils.timezone import localtime

# defino los serializers de mi app inventario, estos serializers son ProductoSerializer, InventarioSerializer y VentaSerializer.

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    productoNombre = serializers.ReadOnlyField(source='producto.nombre')
    productoPrecio = serializers.ReadOnlyField(source='producto.precio')

    class Meta:
        model = Venta
        fields = '__all__'

        # defino una funcion para dar formato a la fecha de la venta que me permita visualizarla en el formato 'dd/mm/yy HH:MM:SS'.

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fecha_bogota = localtime(instance.fecha, pytz.timezone('America/Bogota'))
        representation['fecha'] = fecha_bogota.strftime('%d/%m/%y %H:%M:%S')
        return representation
