from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# defino las rutas de mi app inventario

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'inventarios', views.InventarioViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
