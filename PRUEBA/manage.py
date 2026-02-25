# -----------
# EXPLICACIÓN
# -----------

# 📁 "manage.py" es como el control remoto de tu proyecto. Te permite ejecutar un montón de comandos útiles, como 
# levantar el servidor (runserver), crear una app, hacer migraciones a la base de datos, abrir la consola interactiva de 
# Python, y mucho más. No lo vas a modificar casi nunca, pero lo vas a usar todo el tiempo desde la terminal. 
# Básicamente, es la navaja suiza de Django.

# COMANDOS COMUNES
# ----------------

# 🚀 Para Arrancar y Manejar el Proyecto:
# --------------------------------------  

#   a) "runserver": Este es el primero que vas a usar. Levanta el servidor de desarrollo liviano que trae Django. 
#                   Por defecto, corre acá nomás en tu compu, en la dirección 127.0.0.1:8000. Es una belleza porque se 
#                   actualiza solo cuando guardás cambios en el código, así que ves todo al toque.

#   b) "startapp <nombre_app>": Cuando tu proyecto empiece a crecer, lo ideal es separarlo en aplicaciones (por ejemplo, 
#                               una app para "clientes", otra para "productos"). Este comando te crea la estructura de 
#                               carpetas y archivos básicos (como models.py, views.py) para una nueva app, todo limpito 
#                               y ordenado.

#   c) "createsuperuser": Este es el que te da la llave del panel de administración de Django (ese /admin que vimos). 
#                         Te guía paso a paso para crear un usuario con superpoderes, que puede manejar usuarios, 
#                         contenidos y todo lo que se te ocurra desde la interfaz admin.

# 🗄️ Para Manejar la Base de Datos:
# --------------------------------

#   a) "makemigrations": Cuando toqueteás los modelos (las clases en models.py), Django necesita que le expliques los 
#                        cambios. Este comando se encarga de preparar las instrucciones (las famosas migraciones) para 
#                        que la base de datos entienda cómo tiene que actualizarse. Es como hacer la planificación de la 
#                        obra.

#   b) "migrate": Este es el que ejecuta la obra sobre la base de datos. Toma todas las instrucciones que preparó 
#                 makemigrations y las aplica de verdad, creando tablas, agregando campos, etc. Es fundamental para 
#                 mantener sincronizado tu código con la base de datos.

#   c) "showmigrations": ¿No te acordás qué migraciones ya aplicaste y cuáles están pendientes? Con este comando las ves 
#                        listadas claramente, con un montón de [X] al lado de las que ya están hechas. Ideal para sacarte 
#                        las dudas.

#   d) "sqlmigrate <app> <migracion>": Esto es para los curiosos o para cuando algo no funciona. Te muestra el código 
#                                      SQL puro que se va a ejecutar cuando corras una migración. No cambia nada en la 
#                                      base de datos, solo te deja ver el ADN de la operación.

#   e) "dbshell": Si sos de los que les gusta meter mano directamente con SQL, este comando te saca de la interfaz de 
#                 Django y te mete de cabeza en la consola interactiva de tu base de datos (la que tengas configurada, 
#                 sea Postgre, MySQL o SQLite).

#   f) "flush": Un comando bastante fuerte. Le hace un "reset" a la base de datos, borrando toda la información que hay 
#               en las tablas, pero dejando la estructura (las tablas mismas) intactas. Ojo con usarlo en producción, 
#               porque los datos se te van para siempre.

# 🧪 Para Probar y Depurar:
# ------------------------

#   a) "shell": Te abre una consola interactiva de Python, pero con todo el entorno de Django ya cargado. Es un lujo 
#               para probar cositas, hacer consultas a la base de datos al vuelo, o testear funciones sin tener que 
#               levantar todo el sitio.

#   b) "test": Si escribiste pruebas automáticas para tu aplicación (cosa que está buenísima hacer), este comando las 
#              ejecuta todas de una. Te asegura que todo lo que ya andaba bien, siga andando bien después de tus cambios.

#   c) "check": Un comando re tranqui que revisa tu proyecto entero en busca de problemas comunes, como errores de 
#               sintaxis en los modelos, configuración rara, etc.

#   d) "iffsettings": ¿Modificaste tantas cosas en settings.py que ya no te acordás cuál era el valor por defecto de 
#                     Django? Este comando te muestra las diferencias, para que veas todo de un vistazo.

# 📦 Para Mover Datos y Archivos:
# ------------------------------

#   a) "dumpdata": Hace una "foto" de toda la información de tu base de datos y la guarda en un archivo, generalmente 
#                  en formato JSON. Sirve para hacer copias de seguridad o para pasar datos de un lado a otro.

#   b) "loaddata": Es la contracara del anterior. Toma un archivo de datos (como el que genera dumpdata) y lo mete en 
#                  tu base de datos. Muy útil para cargar datos de prueba o recuperar información.

#   c) "collectstatic": Cuando termines tu sitio y lo subas a un servidor de verdad, necesitás juntar todos los archivos 
#                       estáticos (CSS, JavaScript, imágenes) de todas tus apps en una sola carpeta. Este comando hace 
#                       ese trabajito de organización por vos.

# --------------------------------------------------------------------------------------------------------------------- #


#!/usr/bin/env python
# Django's command-line utility for administrative tasks.


import os
import sys


def main():
    # Run administrative tasks.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRUEBA.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()