# =================================================
# 🐍☁️📦🧬🎭 TUTORIAL DE POO EN PYTHON 🎭🧬📦☁️🐍
# =================================================

import os
import sys

# Configuración para que los emojis se vean bien en Windows.
if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')
    os.system('color') 

sys.stdout.reconfigure(encoding='utf-8')


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
# CLASES PARA LOS EJEMPLOS (los moldes)
# -------------------------------------

class Animal:
    def respirar(self):
        return "Estoy respirando... 🫁"


class Perro(Animal):
    # Atributo de Clase (Ejemplo 9).
    especie = "Canino"

    def __init__(self, nombre, edad, raza="Callejero"):
        self.nombre = nombre  # Atributo de instancia.
        self.edad = edad      # Atributo de instancia.
        self.raza = raza


    def ladrar(self):
        return f"¡Guau! Soy {self.nombre} y tengo {self.edad} años. 🐶"

    # Método especial (Ejemplo 10).
    def __str__(self):
        return f"Objeto Perro: {self.nombre} ({self.raza})"


class Gato(Animal):
    def maullar(self):
        return "¡Miau! 🐱"


class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial # Atributo Privado (Ejemplo 4).

    def ver_saldo(self):
        return f"Saldo actual: ${self.__saldo} 💰"
    

# DEFINICIÓN DE LOS 10 EJEMPLOS
# -----------------------------

def ejemplo1():
    print("\n🏗️ EJEMPLO 1: LA CLASE Y EL OBJETO")
    print("===================================\n")
    print("La clase es el molde 'Perro'. El objeto es 'mi_pichicho'.")
    
    class PerroSimple: pass
    mi_pichicho = PerroSimple()
    print(f"Objeto creado: {mi_pichicho}")
    print("\nNO TE ASUSTES!👀" 
          "\nEse output es la identidad digital del objeto. Te dice qué es y dónde está, pero como" 
          "\ntodavía no le dimos 'personalidad', se presenta con su número de serie de fábrica. 🏭")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo2():
    print("\n🛠️ EJEMPLO 2: EL CONSTRUCTOR (__init__)")
    print("=======================================\n")
    
    pichicho = Perro("Albóndiga", 3)
    print(f"El perro {pichicho.nombre} nació gracias al constructor.")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo3():
    print("\n🏃 EJEMPLO 3: MÉTODOS (ACCIONES)")
    print("================================\n")
    
    pichicho = Perro("Albóndiga", 3)
    print(f"Acción del perro: {pichicho.ladrar()}")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo4():
    print("\n🏰 EJEMPLO 4: ENCAPSULAMIENTO")
    print("=============================\n")
    
    caja = CuentaBancaria(1000)
    print(caja.ver_saldo())
    print("💡 No podés ver 'caja.__saldo' directamente, está protegido.")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo5():
    print("\n👑 EJEMPLO 5: HERENCIA")
    print("======================\n")
    
    minino = Gato()
    print(f"Heredado de Animal: {minino.respirar()}")
    print(f"Propio de Gato: {minino.maullar()}")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo6():
    print("\n🎭 EJEMPLO 6: POLIMORFISMO")
    print("==========================\n")
    
    animales = [Perro("Albóndiga", 2), Gato()]
    print("Hacemos que todos 'respiren' aunque sean distintos:")
    for a in animales:
        print(f"- {a.respirar()}")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo7():
    print("\n🎨 EJEMPLO 7: ABSTRACCIÓN")
    print("=========================\n")
    print("Solo nos importa que el Perro ladre, no cómo funcionan sus cuerdas vocales.")
    
    p = Perro("Panchi", 5)
    print(p.ladrar())
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo8():
    print("\n📝 EJEMPLO 8: LISTA DE OBJETOS")
    print("==============================\n")
    
    jauria = [Perro("Manchita", 1), Perro("Luna", 4), Perro("Lobo", 8)]
    for p in jauria:
        print(f"Cuidando a: {p.nombre}")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo9():
    print("\n👔 EJEMPLO 9: ATRIBUTOS DE CLASE")
    print("================================\n")
    
    p1 = Perro("A", 1)
    p2 = Perro("B", 2)
    print(f"P1 es: {p1.especie}, P2 es: {p2.especie}")
    print("💡 El atributo 'especie' es compartido por todos los perros.")
    input("\nPresioná Enter para seguir...")
    
    
def ejemplo10():
    print("\n🌀 EJEMPLO 10: MÉTODO ESPECIAL __STR__")
    print("======================================\n")
    
    p = Perro("Albóndiga", 10, "Ovejero")
    print("Si imprimo el objeto directamente:")
    print(p)
    input("\nPresioná Enter para seguir...")
    

# MENÚ PRINCIPAL
# --------------

def mostrar_menu():
    print("\n==================================================\n")
    print("         🏰 MENÚ DEL TUTORIAL DE POO 🏰   \n")
    print("==================================================\n")
    print("1.  🏗️ El Molde (Clase y Objeto básico)")
    print("2.  🛠️ El Nacimiento (Constructor __init__)")
    print("3.  🏃 Acciones (Métodos)")
    print("4.  🏰 Caja Fuerte (Encapsulamiento)")
    print("5.  👑 Legado (Herencia)")
    print("6.  🎭 Identidad (Polimorfismo)")
    print("7.  🎨 Lo importante (Abstracción)")
    print("8.  📝 Lista de Objetos (Manejo de colecciones)")
    print("9.  👔 Atributos de Clase (Variables globales)")
    print("10. 🌀 El Método __str__ (Presentación)")
    print("0.  👋 Salir")
    print("\n==================================================")


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
        print("\n👋 ¡Chau! Ya sos un maestro de los objetos.")
        break
    else:
        input("❌ Opción todavía no implementada o no válida... Enter para volver.")