import os
import sys

if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')
    os.system('color') 

sys.stdout.reconfigure(encoding='utf-8')

# ================================================
# 📚 ¿QUÉ ES LA PROGRAMACIÓN ORIENTADA A OBJETOS?
# ================================================

# POO es un paradigma de programación que organiza el código en "objetos" que contienen datos (atributos) y 
# funciones (métodos). Es como crear "fichas" con características y comportamientos propios.

# 🎯 CLASES Y OBJETOS - FUNDAMENTOS
# ==================================

# ¿Qué es una Clase?
# ------------------
# Una clase es como un molde o plantilla para crear objetos. Define qué atributos y métodos tendrán los objetos 
# de ese tipo.

# ¿Qué es un Objeto?
# ------------------
# Un objeto es una instancia específica creada a partir de una clase. Es como el "producto final" hecho con ese molde.


# ===============================
# 🐶 EJEMPLO BÁSICO: CLASE PERRO 
# ===============================

print('\n=================================\n'
      '🐶 EJEMPLO BÁSICO: CLASE PERRO'
      '\n=================================\n')

class Perro:
    # CONSTRUCTOR: se ejecuta al crear un nuevo perro.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo.
        self.edad = edad      # Atributo.
    
    # MÉTODO: comportamiento del perro.
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")
    
    def cumplir_años(self):
        self.edad += 1
        print(f"¡{self.nombre} ahora tiene {self.edad} años!")

# Creando objetos (instancias de la clase Perro).
mi_perro = Perro("Albóndiga", 3)
tu_perro = Perro("Luna", 2)

# Usando los objetos.
mi_perro.ladrar()        # SALIDA: Albóndiga dice: ¡Guau guau!
mi_perro.cumplir_años() # SALIDA: Albóndiga ahora tiene 4 años!
tu_perro.ladrar()        # SALIDA: Luna dice: ¡Guau guau!

print('\n')


#============================================
# 🏠 EJEMPLO PRÁCTICO: SISTEMA DE BIBLIOTECA
#============================================

# Veamos un ejemplo más completo para entender mejor los conceptos:

print('\n============================================\n'
      '🏠 EJEMPLO PRÁCTICO: SISTEMA DE BIBLIOTECA'
      '\n============================================\n')

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Por defecto, nuevo libro está disponible.
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"📖 El libro '{self.titulo}' ha sido prestado.")
            return True
        else:
            print(f"❌ El libro '{self.titulo}' no está disponible.")
            return False
    
    def devolver(self):
        self.disponible = True
        print(f"✅ El libro '{self.titulo}' ha sido devuelto.")
    
    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"📚 Título: {self.titulo}")
        print(f"✍️ Autor: {self.autor}")
        print(f"🔖 ISBN: {self.isbn}")
        print(f"📌 Estado: {estado}")

# Usando la clase.
libro1 = Libro("Neuromante", "William Gibson", "978-0-441-56959-2")
libro2 = Libro("1984", "George Orwell", "978-84-9759-329-8")

# Interactuando con los objetos.
libro1.informacion()
print("-" * 30)
libro1.prestar()
libro1.prestar()  # Intento prestar el mismo libro otra vez.
libro1.devolver()

print('\n')


# ========================
# 🏗️ LOS 4 PILARES DE POO
# ========================

# 1. ENCAPSULAMIENTO 🔒
# =====================

#Protege los datos para que no sean modificados directamente desde fuera de la clase.

print('\n==================================\n'
      'PILARES DE POO: ENCAPSULAMIENTO 🔒'
      '\n==================================\n')

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (doble guión bajo).
        self.__movimientos = []       # Lista privada de movimientos.
    
    # GETTER -> obtiene saldo de forma controlada.
    def obtener_saldo(self):
        return self.__saldo
    
    # SETTER -> modifica saldo de forma controlada.
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self.__movimientos.append(f"Depósito: +${cantidad}")
            print(f"✅ Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("❌ La cantidad debe ser positiva.")
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("❌ La cantidad debe ser positiva.")
        elif cantidad > self.__saldo:
            print("❌ Fondos insuficientes.")
        else:
            self.__saldo -= cantidad
            self.__movimientos.append(f"Retiro: -${cantidad}")
            print(f"✅ Retiro exitoso. Nuevo saldo: ${self.__saldo}")
    
    def mostrar_movimientos(self):
        print(f"📋 Movimientos de {self.titular}:")
        for movimiento in self.__movimientos:
            print(f"  {movimiento}")

# Ejemplo de uso:
# ---------------
cuenta = CuentaBancaria("Silvina Brujilda", 1000)
# print(cuenta.__saldo)  # ❌ Error - no podemos acceder directamente.
print(f"Saldo actual: ${cuenta.obtener_saldo()}")  # ✅ Usando el getter.
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_movimientos()

print('\n')


# 2. HERENCIA 👨‍👦
# ==============

# Crea clases basadas en otras clases, heredando sus atributos y métodos.

print('\n===========================\n'
      'PILARES DE POO: HERENCIA 👨‍👦'
      '\n===========================\n')

# CLASE PADRE: Vehiculo.
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print(f"🚗 {self.marca} {self.modelo} encendido.")
    
    def apagar(self):
        self.encendido = False
        print(f"🚗 {self.marca} {self.modelo} apagado.")
    
    def info_basica(self):
        return f"{self.marca} {self.modelo} ({self.año})"

# CLASE HIJA: Hereda de Vehiculo.
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)  # Llamamos al constructor del padre.
        self.num_puertas = num_puertas
        self.maletero_abierto = False
    
    def abrir_baul(self):
        if self.encendido:
            print("❌ No se puede abrir el baúl con el coche encendido.")
        else:
            self.maletero_abierto = True
            print("✅ Baúl abierto.")
    
    def info_completa(self):
        info_base = self.info_basica()
        return f"{info_base} - {self.num_puertas} puertas."

# OTRA CLASE HIJA.
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # "Deportiva", "Cruiser", etc.
        self.caballete = False
    
    def hacer_willy(self):
        if self.encendido:
            print(f"🏍️ ¡La {self.marca} {self.modelo} haciendo willy!")
        else:
            print("❌ La moto debe estar encendida.")
    
    def info_completa(self):
        return f"{self.info_basica()} - Tipo: {self.tipo}"

# Usando las clases.
mi_coche = Coche("Ford", "Mustang", 2026, 4)
mi_moto = Moto("Honda", "Rebel", 2021, "Cruiser")

print(mi_coche.info_completa())
mi_coche.encender()
mi_coche.abrir_baul()  # No se puede con el coche encendido.
mi_coche.apagar()
mi_coche.abrir_baul()  # Ahora sí.

print("\n" + "-" * 30)
print(mi_moto.info_completa())
mi_moto.encender()
mi_moto.hacer_willy()

print('\n')


# 3. POLIMORFISMO 🔄
# ==================

# Métodos con el mismo nombre pero comportamientos diferentes según la clase.

# PILARES DE POO: POLIMORFISMO 🔄
# ===============================

print('\n===============================\n'
      'PILARES DE POO: POLIMORFISMO 🔄'
      '\n===============================\n')

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Método vacío que será sobreescrito.

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau miau!"
    
    def ronronear(self):
        return "purr purr..."

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"
    
    def mover_cola(self):
        return "moviendo la cola felizmente!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu muuu!"

# DEMOSTRACIÓN DE POLIMORFISMO.
def presentar_animal(animal):
    # Esta función funciona con cualquier animal.
    print(f"🐾 {animal.nombre} dice: {animal.hacer_sonido()}")
    
    # Cada animal puede tener comportamientos específicos.
    if isinstance(animal, Gato):
        print(f"   y también {animal.ronronear()}")
    elif isinstance(animal, Perro):
        print(f"   y también {animal.mover_cola()}")

# Crea diferentes animales.
animales = [
    Gato("Garfield"),
    Perro("Albóndiga"),
    Vaca("Yolanda")
]

# El mismo método se comporta diferente según el animal.
for animal in animales:
    presentar_animal(animal)
    print()
    
print('\n')


# 4. ABSTRACCIÓN 🎭
# =================

# Oculta la complejidad interna y muestra solo lo necesario.

print('\n==============================\n'
      'PILARES DE POO: ABSTRACCIÓN 🎭'
      '\n==============================\n')

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    # CLASE ABSTRACTA -> No se puede instanciar directamente.
    
    @abstractmethod
    def area(self):
        # MÉTODO ABSTRACTO -> Debe ser implementado por las clases hijas.
        pass
    
    @abstractmethod
    def perimetro(self):
        # MÉTODO ABSTRACTO -> Debe ser implementado por las clases hijas.
        pass
    
    def descripcion(self):
        # MÉTODO CONCRETO -> Ya tiene implementación.
        return f"Soy una figura con área {self.area():.2f} y perímetro {self.perimetro():.2f}"

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# USANDO LAS CLASES.
# figura => FiguraGeometrica()  # ❌ Error -> No se puede instanciar clase abstracta.

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print("🔴 Círculo:")
print(f"  Área: {circulo.area():.2f}")
print(f"  Perímetro: {circulo.perimetro():.2f}")
print(f"  {circulo.descripcion()}")

print("\n📏 Rectángulo:")
print(f"  Área: {rectangulo.area()}")
print(f"  Perímetro: {rectangulo.perimetro()}")
print(f"  {rectangulo.descripcion()}")

print('\n')


# ===============================
# 📝 RESUMEN Y MEJORES PRÁCTICAS
# ===============================

# CONCEPTOS CLAVE:
# ----------------

# 🔹CLASE: Plantilla para crear objetos.

# 🔹OBJETO: Instancia de una clase.

# 🔹ATRIBUTOS: Características del objeto.

# 🔹MÉTODOS: Comportamientos del objeto.

# 🔹CONSTRUCTOR (__init__): Inicializa nuevos objetos.

# 🔹self: Referencia al propio objeto.

# BUENAS PRÁCTICAS:
# ----------------

# 1. Nombres descriptivos para clases (sustantivos, CamelCase).

# 2. Métodos con nombres de acciones (verbos, snake_case).

# 3. Encapsular datos que no deban modificarse directamente.

# 4. Usar herencia solo cuando tenga sentido lógico.

# 5. Mantener clases pequeñas y con una sola responsabilidad.

# 6. Documentar el propósito de clases y métodos.

# CUÁNDO USAR POO:
# ----------------

# 🔹Sistemas complejos con muchas entidades relacionadas.

# 🔹Cuando necesitas modelar objetos del mundo real.

# 🔹Para reutilizar código mediante herencia.

# 🔹Cuando trabajas en equipo (organiza mejor el código).

print("\n===========================================================\n"
      "GRACIAS POR UTILIZAR ESTE PEQUEÑO TUTORIAL DE POO EN PYTHON\n" 
      "   ¡SEGUÍ PRACTICANDO Y CREANDO COSAS INCREÍBLES! 🚀"
      "\n===========================================================\n")