# -----------
# EXPLICACIÓN
# -----------

# 🔌 "asgi.py" es parecido al 'wsgi.py', pero para lo nuevo: aplicaciones en tiempo real, como chats, notificaciones en 
# vivo, o websockets. ASGI (Asynchronous Server Gateway Interface) es la versión moderna y asincrónica. Si no vas a 
# hacer nada en tiempo real, probablemente no lo necesites por ahora, pero está ahí por si algún día querés sumar esas 
# funcionalidades.

# --------------------------------------------------------------------------------------------------------------------- #


# ASGI config for Prueba project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see:
# https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRUEBA.settings')

application = get_asgi_application()