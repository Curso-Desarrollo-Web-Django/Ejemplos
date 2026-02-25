# -----------
# EXPLICACIÓN
# -----------

# 👁️ "views.py" este es otro archivo clave. Las vistas son las funciones (o clases) que deciden qué mostrar cuando 
# alguien entra a una dirección. Reciben una solicitud (un request) y devuelven una respuesta (un response), que 
# generalmente es una página web. Acá va toda la lógica: buscar cosas en la base de datos, procesar formularios, 
# preparar la información para mostrarla, etc. Es el cerebro que decide qué pasa cuando alguien visita tu app.

# --------------------------------------------------------------------------------------------------------------------- #


# Cambia from django.shortcuts import render (el original)
# por from django.http import HttpResponse.
from django.http import HttpResponse

# Create your views here.

# 📌 VISTA DE PRUEBA
# -------------------
# Función que se ejecuta cuando alguien visita nuestra página.
#def saludo(request): # request: contiene información de la petición del usuario.
#   return HttpResponse("¡Hola Mundo! Esta es mi primera aplicación en Django 🎉") 
# return HttpResponse("...") Devuelve un mensaje que mostrará el navegador.

# 📌 VISTA MEJORADA UTILIZANDO HTTP CON HTML Y CSS EMBEBIDO
# ----------------------------------------------------------
def saludo(request):
    html_content = """
    <!DOCTYPE html>
        <html lang="es">
        
            <head>
                <meta charset="UTF-8">
                    <style>
                        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Roboto:wght@400&display=swap');
                        
                        body {
                            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                            height: 100vh;
                            margin: 0;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            font-family: 'Roboto', sans-serif;
                            color: white;
                            text-align: center;
                            }
                            
                        .container {
                                    background: rgba(255, 255, 255, 0.1);
                                    padding: 3rem;
                                    border-radius: 20px;
                                    backdrop-filter: blur(10px);
                                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                                    border: 1px solid rgba(255, 255, 255, 0.18);
                                }
                                
                        h1 {
                            font-family: 'Poppins', sans-serif;
                            font-size: 4rem;
                            margin-bottom: 10px;
                            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                        }
                        
                        h2 {
                            font-size: 2rem;
                            color: #00d4ff;
                            font-weight: 300;
                        }
                        
                        .emoji {
                                font-size: 5rem;
                                margin-bottom: 20px;
                            }
                    </style>
            </head>
        
            <body>
                <div class="container">
                    <div class="emoji">🚀</div>
                    <h1>¡Esto es una prueba!</h1>
                    <h2>Hola Mundo en Django ✨</h2>
                </div>
            </body>
            
        </html>
    """
    return HttpResponse(html_content)