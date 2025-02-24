from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.files.storage import default_storage
import logging
from .models import Producto, Inventario, Venta
from .serializers import ProductoSerializer, InventarioSerializer, VentaSerializer

logger = logging.getLogger(__name__)

# Generate the views for the inventario app using Django Rest Framework.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Log the incoming request data
            logger.info(f"Received data: {request.data}")
            
            # Handle multipart form data
            data = request.data.copy()
            image_file = request.FILES.get('imagen')
            
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                # Handle image upload separately if present
                if image_file:
                    try:
                        path = default_storage.save(f'productos/{image_file.name}', image_file)
                        data['imagen'] = path
                    except Exception as e:
                        logger.error(f"Image upload error: {str(e)}")
                        return Response(
                            {'error': 'Failed to upload image'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )

                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Validation errors: {serializer.errors}")
                return Response(
                    {'error': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            logger.error(f"Error creating product: {str(e)}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
