from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'inventarios', views.InventarioViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete_product/<int:product_id>/', views.delete_product_view, name='delete-product'),
]
