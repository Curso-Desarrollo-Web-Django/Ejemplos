from django.shortcuts import render
# ➕ AGREGADO: Importamos el modelo Producto para poder consultar la base de datos.
from .models import Producto

# Create your views here.

def listado_productos(request):
    
    # Vista que obtiene todos los productos de la base de datos y los envía al 
    # template para ser mostrados.
    
    # Flujo de datos:
    #     1. Recibe un request HTTP
    #     2. Consulta todos los registros de Producto (SELECT * FROM productos_producto).
    #     3. Prepara un diccionario con el contexto (los datos a enviar al template).
    #     4. Renderiza el template 'productos.html' con ese contexto.
    #     5. Devuelve la respuesta HTTP al navegador.
    
    # ➕ AGREGADO: Obtenemos todos los productos de la base de datos.
    # Esto ejecuta: SELECT * FROM productos_producto;
    productos = Producto.objects.all()
    
    # ➕ AGREGADO: Creamos un diccionario con los datos para pasar al template.
    # La clave 'productos' es la que vamos a usar en el template.
    contexto = {
        'productos': productos,
    }
    
    # ➕ AGREGADO: Renderizamos el template y le pasamos el contexto.
    return render(request, 'productos.html', contexto)

# =========================================================================== #
# 🧉 EXPLICACIÓN: Esta vista es lo más básico que podemos hacer:
# traer todos los registros de una tabla y mostrarlos.
# Producto.objects.all() es el equivalente a SELECT * FROM productos_producto.
# El diccionario 'contexto' es la comunicación entre la vista y el template.
# =========================================================================== #