# -----------
# EXPLICACIÓN
# -----------

# ➕ "urls.py" fijate que cuando se crea la app, Django no pone un archivo urls.py automáticamente. Lo tenés que crear 
# vos. ¿Por qué? Porque las rutas de la app se conectan después con el urls.py principal del proyecto. Entonces, es una 
# práctica re común crear un archivo urls.py dentro de HolaMundo para manejar todas las rutas que empiecen con 
# /holamundo/. Después, en el urls.py principal, vinculás todo con un include(). Es como armar un mapa chico para la app 
# y después pegarlo en el mapa grande del proyecto.

# --------------------------------------------------------------------------------------------------------------------- #


from django.urls import path
from . import views  # Importa las vistas de esta misma carpeta.

# Define las URLs de nuestra aplicación.
urlpatterns = [
    # URL vacía ejecuta la vista 'saludo'.
    path('', views.saludo, name='saludo'),
]