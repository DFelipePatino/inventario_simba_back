import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import localtime
import pytz

# Define the models that will be synchronized with the database for the inventario_simba project. These models are Producto, Inventario, and Venta.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='Descripción por defecto')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def delete_product(self):
        if hasattr(self, 'inventario'):
            self.inventario.delete()
        self.venta_set.all().delete()
        self.delete()

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.producto.stock = self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if self.producto.stock < self.cantidad:
            raise ValidationError('No hay suficiente stock para completar la venta.')
        self.producto.stock -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)

    @property
    def productoNombre(self):
        return self.producto.nombre
    
    # Define a function to format the sale date.
    def __str__(self):
        fecha_bogota = localtime(self.fecha, pytz.timezone('America/Bogota'))
        formatted_date = fecha_bogota.strftime('%d/%m/%y %H:%M:%S')
        return f"{self.producto.nombre} - {self.cantidad} - {formatted_date}"
