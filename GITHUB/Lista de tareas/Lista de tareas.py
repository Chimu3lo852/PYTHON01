# todo.py

# Lista vacía para almacenar las tareas
tareas = []

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

def agregar_tarea():
    """Permite al usuario agregar una nueva tarea a la lista."""
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada correctamente.")

def mostrar_tareas():
    """Muestra todas las tareas en la lista."""
    print("\n--- Tareas Actuales ---")
    if len(tareas) == 0:
        print("No hay tareas en la lista.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tarea():
    """Permite al usuario eliminar una tarea por su número."""
    mostrar_tareas()

    # Verificar si la lista está vacía
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return

    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: "))
        
        # Verificar si el índice está en el rango válido

        if 1 <= indice <= len(tareas):
            tarea_seleccionada = tareas[indice - 1]
            confirmacion = input(f"¿Estás seguro de que deseas eliminar la tarea '{tarea_seleccionada}'? (s/n): ").lower()
            if confirmacion == 's':
                tarea_eliminada = tareas.pop(indice - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Número de tarea no válido. Intenta de nuevo.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            mostrar_tareas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()





