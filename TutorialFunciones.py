# ==========================
# 💻⚙️ ¿QUÉ ES UNA FUNCIÓN?
# ==========================

# Una función es un bloque de código reutilizable que realiza una tarea específica.

# ✅ Ayuda a organizar el código.

# ✅ Evita repetir código.

# ✅ Facilita el mantenimiento y la lectura.


# ====================================
# 📂 ESTRUCTURA BÁSICA DE UNA FUNCIÓN
# ====================================

#def nombre_de_la_funcion(parametros):
    # Cuerpo de la función.
#    return resultado


# =======================
# 🧪 EJEMPLOS EXPLICADOS
# =======================

import os
import sys

if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')
    os.system('color') 

sys.stdout.reconfigure(encoding='utf-8')


def mostrar_menu():
    
    # Función que muestra el menú principal del tutorial.
    # No recibe parámetros.
    # No retorna nada, solo imprime en pantalla.
    
    print("\n===================================\n"
          "📚 TUTORIAL DE FUNCIONES EN PYTHON"
          "\n===================================\n")
    print("1. Función sin parámetros ni retorno")
    print("2. Función con parámetros y sin retorno")
    print("3. Función con parámetros y con retorno")
    print("4. Función con parámetros por defecto")
    print("5. Función que retorna múltiples valores")
    print("6. Función con argumentos variables (*args)")
    print("7. Función con argumentos de palabra clave (**kwargs)")
    print("8. Función lambda (anónima)")
    print("9. Función dentro de otra función")
    print("10. Función recursiva (factorial)")
    print("0. Salir")
    print("======================================================\n")


# 📌 EJEMPLO 1: FUNCIÓN SIN PARÁMETROS NI RETORNO
# ===============================================

def ejemplo1():
    
    # EJEMPLO 1: Función más básica.
    # - SIN parámetros: no recibe datos de entrada.
    # - SIN retorno: no devuelve ningún valor, solo ejecuta código.
    
    print("\n📌 EJEMPLO 1: Función simple sin parámetros ni retorno.")
    print("🔍 EXPLICACIÓN: Esta función solo imprime un mensaje cuando es llamada.")
    
    # Definición de la función dentro del ejemplo.
    def saludar():
        # Cuerpo de la función: lo que hace cuando se llama.
        print("👋 ¡Hola! Soy una función.")
        # No tiene return, por lo que termina aquí.
    
    # Llamada a la función (ejecutamos el código dentro de saludar).
    saludar()
    
    # Pequeña explicación adicional.
    print("✅ Las funciones sin parámetros son útiles para tareas que no necesitan datos externos.")
    
    input("\nPresiona Enter para continuar...")  # Pausa para que el usuario pueda leer.


# 📌 EJEMPLO 2: FUNCIÓN CON PARÁMETROS Y SIN RETORNO
# ===================================================

def ejemplo2():
   
    # EJEMPLO 2: Función que recibe datos pero no devuelve nada.
    # - CON parámetros: recibe nombre como dato de entrada.
    # - SIN retorno: solo imprime, no devuelve valor.
    
    print("\n📌 EJEMPLO 2: Función con parámetros y sin retorno.")
    print("🔍 EXPLICACIÓN: La función recibe un nombre y lo usa para personalizar el saludo.")
    
    # Definición de la función con un parámetro.
    def saludar_persona(nombre):
        
        # Esta función recibe un nombre (parámetro) y lo usa dentro del mensaje.
        
        # El parámetro "nombre" se comporta como una variable dentro de la función.
        print(f"👋 ¡Hola, {nombre}! ¿Cómo estás?")
        # No hay return, la función termina aquí.
    
    # Solicitamos datos al usuario para usarlos como argumento.
    nombre = input("Ingresa un nombre: ")
    
    # Llamamos a la función pasando el nombre como argumento.
    # El valor de "nombre" se copia al parámetro de la función.
    saludar_persona(nombre)
    
    print("✅ Los parámetros permiten que las funciones sean reutilizables con diferentes datos")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 3: FUNCIÓN CON PARÁMETROS Y CON RETORNO
# ===================================================

def ejemplo3():
    
    # EJEMPLO 3: Función que recibe datos y devuelve un resultado.
    # - CON parámetros: recibe dos números.
    # - CON retorno: devuelve el resultado de la suma.
    
    print("\n📌 EJEMPLO 3: Función con parámetros y con retorno.")
    print("🔍 Explicación: La función suma dos números y DEVUELVE el resultado.")
    
    # Definición de la función con dos parámetros y retorno.
    def sumar(a, b):
        
        # Recibe dos números (a y b).
        # Calcula la suma.
        # Retorna (devuelve) el resultado.
        
        resultado = a + b  # Procesamos los datos.
        return resultado   # Devolvemos el resultado (aquí termina la función).
    
    try:  # Manejamos posibles errores si el usuario no ingresa números.
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        
        # Llamamos a la función y GUARDAMOS lo que retorna.
        resultado = sumar(x, y)
        
        # Usamos el valor retornado.
        print(f"✅ La suma de {x} + {y} = {resultado}")
        
        print("📝 Nota: El 'return' permite usar el resultado fuera de la función.")
        
    except ValueError:  # Si ocurre un error al convertir a float.
        print("❌ Error: Ingresa números válidos.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 4: FUNCIÓN CON PARÁMETROS POR DEFECTO
# =================================================

def ejemplo4():
    
    # EJEMPLO 4: Parámetros con valores predeterminados.
    # Si no se proporciona un argumento, usa el valor por defecto.
    
    print("\n📌 EJEMPLO 4: Parámetros por defecto.")
    print("🔍 EXPLICACIÓN: Algunos parámetros tienen valores pre-asignados.")
    
    # Definición con parámetros por defecto.
    def presentar(nombre, edad=18, ciudad="Desconocida"):
        
        # - nombre: obligatorio (sin valor por defecto).
        # - edad: opcional, si no se da usa 18.
        # - ciudad: opcional, si no se da usa "Desconocida".
        
        print(f"🧑 {nombre} tiene {edad} años y vive en {ciudad}.")
    
    # Diferentes formas de llamar a la función.
    print("\n🔹 CASO 1: Solo pasamos el nombre (edad y ciudad usan valores por defecto):")
    presentar("Silvana")
    
    print("\n🔹 CASO 2: Pasamos nombre y edad (ciudad usa valor por defecto):")
    presentar("David", 51)
    
    print("\n🔹 CASO 3: Pasamos todos los argumentos:")
    presentar("Emma", 30, "Estocolmo")
    
    print("\n📝 Los parámetros por defecto deben ir DESPUÉS de los obligatorios.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 5: RETORNO MÚLTIPLE
# ===============================

def ejemplo5():
    
    # EJEMPLO 5: Función que devuelve varios valores.
    # Python permite retornar múltiples valores como una tupla.
    
    print("\n📌 EJEMPLO 5: Retorno múltiple.")
    print("🔍 EXLICACIÓN: Una función puede devolver varios valores separados por comas.")
    
    def operaciones(a, b):
        
        # Realiza varias operaciones y retorna todos los resultados.
        suma = a + b
        resta = a - b
        producto = a * b
        
        # Retornamos múltiples valores separados por comas.
        # Python automáticamente los empaqueta en una tupla.
        return suma, resta, producto
    
    try:
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        
        # Podemos recibir los valores en variables separadas.
        s, r, p = operaciones(x, y)
        
        print(f"➕ Suma: {s}")
        print(f"➖ Resta: {r}")
        print(f"✖️ Producto: {p}")
        
        # También podemos recibir todo como una tupla.
        resultados = operaciones(10, 5)
        print(f"\n📦 Todos los resultados como tupla: {resultados}")
        print(f"   Tipo de dato: {type(resultados)}")
        
    except ValueError:
        print("❌ Error: Ingresa números válidos.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 6: ARGUMENTOS VARIABLES (*args)
# ===========================================

def ejemplo6():
    
    # EJEMPLO 6: *args (argumentos variables).
    # Permite pasar cualquier cantidad de argumentos posicionales.
    
    print("\n📌 EJEMPLO 6: *args - argumentos variables.")
    print("🔍 EXPLICACIÓN: *args permite recibir cualquier número de argumentos.")
    
    def suma_varios(*numeros):
        
        # El * antes del parámetro indica que recibirá múltiples valores.
        # Dentro de la función, "numeros" es una tupla con todos los argumentos.
        
        print(f"📥 Recibí {len(numeros)} argumentos: {numeros}")
        
        # Sumamos todos los números usando la función sum().
        total = sum(numeros)
        return total
    
    # Probamos con diferentes cantidades de argumentos.
    print("\n🔹 Llamada con 5 argumentos:")
    resultado1 = suma_varios(1, 2, 3, 4, 5)
    print(f"✅ Resultado: {resultado1}")
    
    print("\n🔹 Llamada con 3 argumentos:")
    resultado2 = suma_varios(10, 20, 30)
    print(f"✅ Resultado: {resultado2}")
    
    print("\n🔹 Llamada con 1 argumento:")
    resultado3 = suma_varios(100)
    print(f"✅ Resultado: {resultado3}")
    
    print("\n📝 *args es muy útil cuando no sabemos cuántos argumentos recibiremos.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 7: ARGUMENTOS DE PALABRA CLAVE (**kwargs)
# =====================================================

def ejemplo7():
    
    # EJEMPLO 7: **kwargs (keyword arguments).
    # Permite pasar cualquier cantidad de argumentos con nombre.
    
    print("\n📌 EJEMPLO 7: **kwargs - argumentos clave-valor.")
    print("🔍 EXPLICACIÓN: **kwargs recibe argumentos con nombre como diccionario.")
    
    def mostrar_datos(**datos):
        
        # El ** antes del parámetro indica que recibirá argumentos con nombre.
        # Dentro de la función, "datos" es un diccionario.
        
        print(f"📥 Recibí {len(datos)} argumentos con nombre.")
        
        # Recorremos el diccionario para mostrar cada par clave-valor.
        for clave, valor in datos.items():
            print(f"🔹 {clave}: {valor}")
        
        # También podemos acceder a valores específicos si existen.
        if 'nombre' in datos:
            print(f"\n👤 El nombre es: {datos['nombre']}")
    
    print("\n🔹 Llamada con 3 argumentos con nombre:")
    mostrar_datos(nombre="Sebastián", edad=38, ciudad="Mar del Plata")
    
    print("\n🔹 Llamada con 2 argumentos con nombre:")
    mostrar_datos(producto="Laptop", precio=1200)
    
    print("\n📝 **kwargs es perfecto para configuraciones y opciones flexibles")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 8: FUNCIÓN LAMBDA
# =============================

def ejemplo8():
    
    # EJEMPLO 8: Funciones lambda (anónimas).
    # Funciones pequeñas y temporales de una sola línea.
    
    print("\n📌 EJEMPLO 8: Lambda - función anónima.")
    print("🔍 EXPLICACIÓN: Las funciones lambda son expresiones rápidas de una línea.")
    
    # Sintaxis: lambda parámetros: expresión.
    # Creación de una función lambda para multiplicar.
    multiplicar = lambda x, y: x * y
    
    print("📝 Creamos: multiplicar = lambda x, y: x * y")
    print("   Esto es equivalente a:")
    print("   def multiplicar(x, y):")
    print("       return x * y")
    
    try:
        a = float(input("\nIngresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        
        # Usamos la función lambda.
        resultado = multiplicar(a, b)
        print(f"✖️ {a} * {b} = {resultado}")
        
        # Las lambdas también se pueden usar sin asignarlas a variables.
        print("\n🔹 Lambda usada directamente:")
        print(f"   (lambda x: x**2)(5) = {(lambda x: x**2)(5)}")
        
        # EJEMPLO PRÁCTICO: ordenar usando lambda.
        personas = [("Carolina", 22), ("David", 51), ("Lourdes", 52)]
        ordenadas = sorted(personas, key=lambda persona: persona[1])  # Ordena por edad.
        print(f"\n🔹 Ordenando lista por edad con lambda: {ordenadas}")
        
    except ValueError:
        print("❌ Error: Ingresa números válidos.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 9: FUNCIÓN DENTRO DE OTRA FUNCIÓN
# =============================================

def ejemplo9():
    
    # EJEMPLO 9: Funciones anidadas (closures).
    # Una función definida dentro de otra función.
    
    print("\n📌 EJEMPLO 9: Función interna (closure).")
    print("🔍 EXPLICACIÓN: Podemos definir funciones dentro de funciones.")
    
    def operacion_externa(operador):
        
        # Esta función externa recibe un operador como argumento (ej: "suma" o "resta")
        # y devuelve una función interna que realiza la operación.
        
        print(f"🔹 Función externa recibe operador: '{operador}'")
        
        # Definimos funciones internas.
        def suma(x, y):
            return x + y
        
        def resta(x, y):
            return x - y
        
        # La función externa retorna UNA de las funciones internas.
        if operador == "suma":
            print("   Retornando función 'suma'.")
            return suma
        elif operador == "resta":
            print("   Retornando función 'resta'.")
            return resta
        else:
            print("   Operador no válido, retornando None.")
            return None
    
    # Obtenemos la función suma.
    print("\n🔹 Paso 1: Crear función suma.")
    funcion_suma = operacion_externa("suma")
    
    # Usamos la función obtenida.
    print("\n🔹 Paso 2: Usar la función suma.")
    resultado1 = funcion_suma(5, 3)
    print(f"   funcion_suma(5, 3) = {resultado1}")
    
    # Obtenemos la función resta.
    print("\n🔹 Paso 3: Crear función resta.")
    funcion_resta = operacion_externa("resta")
    
    # Usamos la función obtenida.
    print("\n🔹 Paso 4: Usar la función resta.")
    resultado2 = funcion_resta(5, 3)
    print(f"   funcion_resta(5, 3) = {resultado2}")
    
    print("\n📝 Esto se llama 'closure': la función interna recuerda el entorno donde fue creada.")
    
    input("\nPresiona Enter para continuar...")


# 📌 EJEMPLO 10: FUNCIÓN RECURSIVA
# =================================

def ejemplo10():
    
    # EJEMPLO 10: Recursividad.
    # Una función que se llama a sí misma.
    
    print("\n📌 EJEMPLO 10: Recursividad - Factorial.")
    print("🔍 EXPLICACIÓN: Una función recursiva se llama a sí misma para resolver un problema.")
    
    def factorial(n):
        
        # Calcula el factorial de n (n!).
        # Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
        
        print(f"   🟢 Calculando factorial({n})")
        
        # CASO BASE: condición que detiene la recursión.
        if n == 0 or n == 1:
            print(f"      ✅ Caso base: factorial({n}) = 1")
            return 1
        else:
            # PASO RECURSIVO: la función se llama a sí misma.
            print(f"      🔄 {n} * factorial({n-1})")
            resultado_parcial = factorial(n - 1)
            resultado = n * resultado_parcial
            print(f"      🔵 factorial({n}) = {n} * {resultado_parcial} = {resultado}")
            return resultado
    
    try:
        num = int(input("Ingresa un número entero positivo: "))
        
        if num < 0:
            print("❌ El factorial no está definido para números negativos.")
        else:
            print(f"\n📊 Calculando {num}! paso a paso:")
            print("="*40)
            resultado_final = factorial(num)
            print("="*40)
            print(f"✅ El factorial de {num} es {resultado_final}")
            
            # Explicación del proceso.
            print("\n📝 Proceso recursivo:")
            print(f"   {num}! = ", end="")
            for i in range(num, 0, -1):
                print(f"{i}", end=" * " if i > 1 else " = ")
            print(resultado_final)
            
    except ValueError:
        print("❌ Error: Ingresa un número entero válido.")
    
    input("\nPresiona Enter para continuar...")


# 💻 PROGRAMA PRINCIPAL
# ======================

def main():
    
    # Función principal del programa.
    # Controla el menú y la ejecución de los ejemplos.
    
    while True:  # Bucle infinito hasta que el usuario elija salir.
        
        # Limpiamos la pantalla según el sistema operativo.
        # 'cls' para Windows, 'clear' para Linux/Mac.
        os.system('cls' if os.name == 'nt' else 'clear')
        
        mostrar_menu()  # Mostramos el menú.
        
        # Solicitamos la opción al usuario.
        opcion = input("🔍 Elige una opción (0-10): ")
        
        # Estructura condicional para ejecutar el ejemplo seleccionado.
        if opcion == '1':
            ejemplo1()  # Función simple.
        elif opcion == '2':
            ejemplo2()  # Función con parámetros.
        elif opcion == '3':
            ejemplo3()  # Función con retorno.
        elif opcion == '4':
            ejemplo4()  # Parámetros por defecto.
        elif opcion == '5':
            ejemplo5()  # Retorno múltiple.
        elif opcion == '6':
            ejemplo6()  # *args.
        elif opcion == '7':
            ejemplo7()  # **kwargs.
        elif opcion == '8':
            ejemplo8()  # Lambda.
        elif opcion == '9':
            ejemplo9()  # Función interna.
        elif opcion == '10':
            ejemplo10()  # Recursividad.
        elif opcion == '0':
            # Opción de salida.
            print("\n👋 ¡GRACIAS POR USAR EL TUTORIAL DE FUNCIONES EN PYTHON! ¡HASTA PRONTO!👋")
            break  # Rompe el bucle while y termina el programa.
        else:
            # Opción no válida.
            input("❌ Opción no válida. Presiona Enter para continuar...")

# Este condicional verifica si el script se ejecuta directamente (no cuando es importado como módulo).
if __name__ == "__main__":
    main()  # Llama a la función principal.