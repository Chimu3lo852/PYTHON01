# Funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# Mensaje inicial y menú
print("Calculadora Básica")
print("Operaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Input del usuario
opcion = input("Elige una opción (1/2/3/4): ")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Condicionales para elegir la operación
if opcion == "1":
    resultado = sumar(a, b)
    print("Resultado:", resultado)
elif opcion == "2":
    resultado = restar(a, b)
    print("Resultado:", resultado)
elif opcion == "3":
    resultado = multiplicar(a, b)
    print("Resultado:", resultado)
elif opcion == "4":
    if b == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = dividir(a, b)
        print("Resultado:", resultado)
else:
    print("Opción inválida")
