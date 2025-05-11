import random
import os

# Bucle principal para reiniciar el juego
while True:
    # Limpiar la terminal al inicio
    os.system('cls' if os.name == 'nt' else 'clear')

    # Menú de selección de dificultad
    print("Bienvenido al juego de adivinar el número.")
    print("Selecciona la dificultad del juego:")
    print("1. Fácil (15 intentos)")
    print("2. Medio (10 intentos)")
    print("3. Difícil (5 intentos)")

    while True:
        try:
            dificultad = int(input("Introduce el número de la dificultad (1, 2 o 3): "))
            if dificultad == 1:
                numero_secreto = random.randint(1, 100)
                max_intentos = 15
                break
            elif dificultad == 2:
                numero_secreto = random.randint(1, 100)
                max_intentos = 10
                break
            elif dificultad == 3:
                numero_secreto = random.randint(1, 100)
                max_intentos = 5
                break
            else:
                print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    # Variables iniciales
    intentos = 0
    adivinado = False

    print(f"He elegido un número del 1 al 100. ¿Puedes adivinar cuál es?")
    print(f"Tienes un máximo de {max_intentos} intentos para adivinar el número.")

    # Bucle principal del juego
    while not adivinado and intentos < max_intentos:
        try:
            intento = int(input("Adivina el número: "))
            intentos += 1

            diferencia = abs(numero_secreto - intento)

            if intento < numero_secreto:
                if diferencia > 20:
                    print("Muy lejos.")
                elif diferencia > 10:
                    print("Cerca.")
                else:
                    print("Muy cerca.")
            elif intento > numero_secreto:
                if diferencia > 20:
                    print("Muy lejos.")
                elif diferencia > 10:
                    print("Cerca.")
                else:
                    print("Muy cerca.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Mensaje final si no adivina
    if not adivinado:
        print(f"Lo siento, has alcanzado el límite de {max_intentos} intentos. El número era {numero_secreto}.")

    # Preguntar si quiere volver a jugar
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").strip().lower()
    if jugar_de_nuevo != "si":
        print("¡Gracias por jugar!.")
        break