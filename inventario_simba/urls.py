from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# defino las rutas de mi proyecto inventario_simba, aqui se definen las rutas de la app inventario y la ruta de la interfaz de administrador de Django.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
