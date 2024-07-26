from rest_framework import serializers
from .models import Producto, Inventario, Venta
import pytz
from django.utils.timezone import localtime

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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert the fecha to the 'America/Bogota' timezone
        fecha_bogota = localtime(instance.fecha, pytz.timezone('America/Bogota'))
        # Format the date and time as specified
        representation['fecha'] = fecha_bogota.strftime('%d/%m/%y %H:%M:%S')
        return representation
