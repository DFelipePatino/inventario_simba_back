import uuid
from django.core.exceptions import ValidationError
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='Descripción por defecto')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def delete_product(self):
        # Delete related Inventario record
        if hasattr(self, 'inventario'):
            self.inventario.delete()
        
        # Delete related Venta records
        self.venta_set.all().delete()
        
        # Delete the product itself
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

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} - {self.fecha}"
