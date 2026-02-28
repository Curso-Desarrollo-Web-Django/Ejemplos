from django.db import models


# Create your models here.
class Producto(models.Model):
    
    # Modelo que representa un producto facturable.
    # Cada instancia de esta clase será un registro en la tabla 'productos_producto'.
    
    # ➕ AGREGADO: Nombre del producto (ej: "Yerba Mate Amanda").
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del producto"
    )
    
    # ➕ AGREGADO: Descripción más detallada (puede ser opcional).
    descripcion = models.TextField(
        blank=True,  # Puede estar vacío.
        null=True,   # Permite NULL en la BD.
        verbose_name="Descripción"
    )
    
    # ➕ AGREGADO: Precio unitario en pesos argentinos.
    precio = models.DecimalField(
        max_digits=10,        # Hasta 99999999.99
        decimal_places=2,      # Dos decimales (centavos).
        verbose_name="Precio (ARS)"
    )
    
    # ➕ AGREGADO: Control de stock.
    stock = models.IntegerField(
        default=0,
        verbose_name="Cantidad en stock"
    )
    
    # ➕ AGREGADO: Fecha de creación (se autocompleta).
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de alta"
    )
    
    # ➕ AGREGADO: Fecha de última modificación (se actualiza solo).
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última modificación"
    )

    def __str__(self):
        
        # Representación en string del objeto (lo que se ve en el admin).
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']  # Orden alfabético por nombre.

    # ============================================================ #
    # 🧉 EXPLICACIÓN: Este modelo define la estructura de nuestros
    # productos. Cada campo tiene un tipo específico que Django
    # traduce al tipo de dato correspondiente en la BD.
    # El método __str__ es clave para que se vea lindo en el admin.
    # ============================================================ #