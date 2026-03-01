# ======================================
# 🐍 TUTORIAL DE FUNCIONES EN PYTHON 🐍
# ======================================

import os
import sys

# Configuración para que los emojis se vean bien en Windows.
if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')
    os.system('color') 

sys.stdout.reconfigure(encoding='utf-8')


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n==============================================\n")
    print("     🚀 MENÚ DEL TUTORIAL DE FUNCIONES 🚀   \n")
    print("==============================================\n")
    print("1.  📢 Saludo simple (Sin parámetros)")
    print("2.  👤 Saludo personalizado (Con parámetros)")
    print("3.  🧮 Calculadora de suma (Con retorno)")
    print("4.  ⚙️ Parámetros fijos (Valores por defecto)")
    print("5.  📦 Combo de resultados (Retorno múltiple)")
    print("6.  🎒 Bolsa de datos (*args)")
    print("7.  🏷️ Etiquetas de datos (**kwargs)")
    print("8.  ⚡ Función express (Lambda)")
    print("9.  🪆 Función Mamushka (Anidada)")
    print("10. 🔄 El rulo infinito (Recursividad)")
    print("0.  👋 Salir")
    print("\n==============================================")

# DEFINICIÓN DE EJEMPLOS
# ----------------------

def ejemplo1():
    print("\n📢 EJEMPLO 1: LA FUNCIÓN BÁSICA")
    print("================================\n")
    
    def saludar():
        print("¡Hola, chabón/a! Soy una función que solo saluda. 👋")
    saludar()
    print("💡 Esta función no necesita que le pases nada para andar.")
    input("\nPresioná Enter para seguir...")


def ejemplo2():
    print("\n👤 EJEMPLO 2: PASANDO DATA")
    print("===========================\n")
    
    def saludar_pibe(nombre):
        print(f"¡Qué hacés, {nombre}! ¿Todo tranqui? 🧉")
    nom = input("¿Cómo te llamás?: ")
    saludar_pibe(nom)
    input("\nPresioná Enter para seguir...")


def ejemplo3():
    print("\n🧮 EJEMPLO 3: DEVOLVIENDO EL RESULTADO")
    print("=======================================\n")
    
    def sumar(a, b):
        return a + b
    res = sumar(10, 5)
    print(f"Le pedí a la función que sume 10 + 5 y me devolvió: {res} ✅")
    input("\nPresioná Enter para seguir...")


def ejemplo4():
    print("\n⚙️ EJEMPLO 4: VALORES POR DEFECTO")
    print("==================================\n")
    
    def cocinar_asado(puntos="A punto"):
        print(f"Tu asado está saliendo: {puntos} 🔥")
    cocinar_asado() # No le pasamos nada, usa el defecto.
    cocinar_asado("Bien cocido") # Acá sí le pasamos.
    input("\nPresioná Enter para seguir...")


def ejemplo5():
    print("\n📦 EJEMPLO 5: EL COMBO (RETORNO MÚLTIPLE)")
    print("=========================================\n")
    
    def operacion(a, b):
        return a + b, a * b
    suma, mult = operacion(5, 4)
    print(f"De una sola función sacamos la suma ({suma}) y la multiplicación ({mult})! 😱")
    input("\nPresioná Enter para seguir...")


def ejemplo6():
    print("\n🎒 EJEMPLO 6: LA BOLSA DE COSAS (*ARGS)")
    print("=======================================\n")
    
    def listar_compras(*cosas):
        print("En el carrito tenemos:")
        for item in cosas:
            print(f"- {item}")
    listar_compras("Yerba", "Azúcar", "Facturas")
    input("\nPresioná Enter para seguir...")


def ejemplo7():
    print("\n🏷️ EJEMPLO 7: LOS KWARGS (CON ETIQUETAS)")
    print("========================================\n")
    
    def mostrar_info(**datos):
        for clave, valor in datos.items():
            print(f"{clave.capitalize()}: {valor}")
    mostrar_info(nombre="Lionel", equipo="Inter Miami", idolo="Messi")
    input("\nPresioná Enter para seguir...")


def ejemplo8():
    print("\n⚡ EJEMPLO 8: FUNCIÓN EXPRESS (LAMBDA)")
    print("======================================\n")
    
    doble = lambda x: x * 2
    print(f"El doble de 10 usando una lambda es: {doble(10)} 🏎️")
    input("\nPresioná Enter para seguir...")


def ejemplo9():
    print("\n🪆 EJEMPLO 9: FUNCIÓN ANIDADA")
    print("=============================\n")
    
    def exterior():
        print("Estoy en la función de afuera...")
        def interior():
            print("...y ahora estoy en la de adentro! 🕵️")
        interior()
    exterior()
    input("\nPresioná Enter para seguir...")


def ejemplo10():
    print("\n🔄 EJEMPLO 10: RECURSIVIDAD (EL FACTORIAL)")
    print("==========================================\n")
    
    def factorial(n):
        if n == 1: return 1
        return n * factorial(n - 1)
    num = 5
    print(f"El factorial de {num} es {factorial(num)}. ¡Magia matemática! 🌀")
    input("\nPresioná Enter para seguir...")


# BUCLE PRINCIPAL
# ---------------

while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("🔍 Elegí una opción (0-10): ")
    
    if opcion == '1': ejemplo1()
    elif opcion == '2': ejemplo2()
    elif opcion == '3': ejemplo3()
    elif opcion == '4': ejemplo4()
    elif opcion == '5': ejemplo5()
    elif opcion == '6': ejemplo6()
    elif opcion == '7': ejemplo7()
    elif opcion == '8': ejemplo8()
    elif opcion == '9': ejemplo9()
    elif opcion == '10': ejemplo10()
    elif opcion == '0':
        print("\n👋 ¡Nos vemos, genio/a! Seguí practicando Python. 🐍")
        break
    else:
        input("❌ Opción no válida... apretá Enter y probá de nuevo.")