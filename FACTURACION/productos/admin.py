from django.contrib import admin
# ➕ AGREGADO: Importamos nuestro modelo Producto.
from .models import Producto

# Register your models here.

# ➕ AGREGADO: Registramos el modelo para que aparezca en el admin.
admin.site.register(Producto)

# ==================================================================== #
# 🧉 EXPLICACIÓN: Con esta simple línea, Django agrega automáticamente
# una interfaz completa para nuestro modelo Producto en el admin.
# Después podemos personalizarla con más opciones, pero por ahora con 
# esto alcanza para empezar a cargar datos.
# ==================================================================== #