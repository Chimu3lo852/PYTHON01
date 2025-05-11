###
# 05 entrada de usuario (input()) 
# la funcion input() permite recibir datos del usuario a traves de la consola
# ###

nombre = input("Hola, ¿cuál es tu nombre?\n")  # la funcion input() recibe un dato del usuario y lo guarda en la variable nombre

print(f"hola {nombre}, encantado de conocerte")

age = input("¿cuántos años tienes?\n")  # la funcion input() recibe un dato del usuario y lo guarda en la variable age
age = int(age)  # convertimos el dato a un entero
print(f"tienes {age} años")  # imprimimos el dato

# UBICACION = input("¿donde vives?\n")  # la funcion input() recibe un dato del usuario y lo guarda en la variable UBIACION
# print(f"vives en {UBICACION}")  # imprimimos el dato

# print("obtener multiples datos de una sola vez")
Estado, Ciudad, = input("¿cual es tu estado, ciudad?\n").split()  # la funcion input() recibe un dato del usuario y lo guarda en la variable Estado, Ciudad, Direccion
print(f"vives en {Estado}, {Ciudad}")  # imprimimos el dato
