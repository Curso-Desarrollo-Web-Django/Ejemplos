# -----------
# EXPLICACIÓN
# -----------

# 🚪 "wsgi.py" este archivo es medio técnico, pero te lo resumo fácil: sirve para cuando subís tu proyecto a internet. 
# WSGI (Web Server Gateway Interface) es el estándar que usa Django para comunicarse con el servidor web (como Apache 
# o Nginx). Mientras estás en tu compu desarrollando, casi ni lo tocás, pero cuando querés que el mundo vea tu página, 
# este archivo se vuelve clave.

# --------------------------------------------------------------------------------------------------------------------- #


# WSGI config for Prueba project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see:
# https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRUEBA.settings')

application = get_wsgi_application()