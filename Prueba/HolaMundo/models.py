# -----------
# EXPLICACIÓN
# -----------

# 🗄️ "models.py" acá definís la estructura de tu base de datos. Cada clase que escribas acá (que hereda de models.Model) 
# se va a convertir en una tabla de la base de datos. Los atributos de la clase son los campos de esa tabla (texto, 
# números, fechas, etc.). En el caso de HolaMundo, podrías tener un modelo Saludo con un campo mensaje y otro fecha. 
# Es el archivo más importante si tu app guarda información.

# --------------------------------------------------------------------------------------------------------------------- #


from django.db import models

# Create your models here.