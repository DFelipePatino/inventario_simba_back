from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define the routes for the project inventario_simba, including the routes for the inventario app and Django's admin interface.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
