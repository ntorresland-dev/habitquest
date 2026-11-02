def mostrar_menu():

    print("\n--- MENÚ DE HÁBITOS ---")
    print("1. Crear nuevo hábito")
    print("2. Listar hábitos")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1, 2 o 3): ").strip()
    return opcion

def crear_habito(habitos, siguiente_id):

    nombre = input("Ingresa el nombre del nuevo hábito: ").strip()
    
    if not nombre:
        print("¡Ups! El nombre del hábito no puede estar vacío. Intenta de nuevo.")
    else:
        habitos[siguiente_id] = nombre
        print(f"¡Excelente! Hábito '{nombre}' creado con el ID {siguiente_id}.")
        siguiente_id += 1  
        
    return siguiente_id

def listar_habitos(habitos):
    if not habitos:
        print("Aún no has creado ningún hábito. ¡Anímate a agregar el primero!")
    else:
        print("\n--- LISTADO DE HÁBITOS ---")
        for id_habito, nombre_habito in habitos.items():
            print(f"ID: {id_habito} | Nombre: {nombre_habito}")

def main():
    
    habitos = {}  
    siguiente_id = 1

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            siguiente_id = crear_habito(habitos, siguiente_id)
            
        elif opcion == '2':
            listar_habitos(habitos)
            
        elif opcion == '3':
            print("¡Hasta luego! Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()