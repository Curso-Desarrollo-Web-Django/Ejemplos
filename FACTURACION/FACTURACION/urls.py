from django.contrib import admin
from django.urls import path
# ✏️ MODIFICACIÓN: Importamos la vista que creamos en la app productos.
from productos.views import listado_productos


urlpatterns = [
    path('admin/', admin.site.urls),
    # ➕ AGREGADO: Ruta para ver el listado de productos.
    # Cuando alguien visite /productos/, Django ejecuta la función
    # listado_productos de productos.views
    path('productos/', listado_productos, name='listado_productos'),
]

# ============================================================== #
# 🧉 EXPLICACIÓN: Cada entrada en urlpatterns es una ruta.
# - El primer argumento es el patrón de URL (sin el dominio).
# - El segundo es la función vista a ejecutar.
# - El tercero (name) es opcional pero muy útil para referenciar
#   esta URL desde otros lugares (templates, redirecciones, etc.)
# ============================================================== #