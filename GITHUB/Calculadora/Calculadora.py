# Funciones matemáticas
def sumar(a: float, b: float):
    return a + b

def restar(a: float, b: float):
    return a - b

def multiplicar(a: float, b: float):
    return a * b

def dividir(a: float, b: float):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

# Muestra el menú al usuario
def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

# Pide dos números al usuario y valida que sean correctos
def pedir_numeros():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print("Error: por favor ingresa números válidos")
        return None, None

# Ejecuta la operación que el usuario eligió
def ejecutar_operacion(opcion, a, b):
    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))

# Función principal que contiene el bucle
def calculadora():
    seguir = "s"
    while seguir == "s":
        mostrar_menu()
        opcion = input("Elige una opción (1/2/3/4): ")

        if opcion in ["1", "2", "3", "4"]:
            a, b = pedir_numeros()
            if a is not None and b is not None:
                ejecutar_operacion(opcion, a, b)
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue  # vuelve al inicio del bucle

        seguir = input("¿Quieres hacer otra operación? (s/n): ").strip().lower()



calculadora()


