# -----------
# EXPLICACIÓN
# -----------

# 🌐 "urls.py" acá se manejan las rutas de tu proyecto. Básicamente, este archivo le dice a Django: "che, si alguien 
# entra a /clientes, mostrale esto", o "si entra a /admin, mostrale el panel de administración". Es como el GPS de tu 
# sitio: redirige cada dirección a su lugar correspondiente.

# --------------------------------------------------------------------------------------------------------------------- #


# URL configuration for Prueba project.

# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/6.0/topics/http/urls/

# EXAMPLES:
# Function views:
#    1. Add an import:  from my_app import views
#    2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views:
#    1. Add an import:  from other_app.views import Home
#    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf:
#    1. Import the include() function: from django.urls import include, path
#    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


from django.contrib import admin
from django.urls import path, include # 🆕 IMPORTAMOS 'include'.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cuando alguien visite /hola/, incluye URLs de HolaMundo.
    path('hola/', include('HolaMundo.urls')),  # 🆕 NUEVA LÍNEA.
]