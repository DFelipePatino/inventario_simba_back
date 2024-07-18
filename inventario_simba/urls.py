from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventario.views import delete_product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')), 
    path('delete_product/<int:product_id>/', delete_product_view, name='delete_product'),
]

# Configuración para servir archivos de medios en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
