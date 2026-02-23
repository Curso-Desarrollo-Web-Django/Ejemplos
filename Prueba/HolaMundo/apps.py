# -----------
# EXPLICACIÓN
# -----------

# 🗺️ "apps.py" este archivo contiene la configuración específica de la app. Tiene una clase que hereda de AppConfig, 
# donde podés ponerle un nombre más lindo a tu app, configurar cosas cuando arranca, etc. La realidad es que no lo vas 
# a tocar mucho al principio, pero Django lo necesita para registrar la app correctamente cuando la activás en el 
# settings.py.

# --------------------------------------------------------------------------------------------------------------------- #


from django.apps import AppConfig


class HolamundoConfig(AppConfig):
    name = 'HolaMundo'