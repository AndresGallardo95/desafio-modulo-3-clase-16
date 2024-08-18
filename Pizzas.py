def mostrar_menu():
    """
    Muestra el menú principal del sistema de personalización de pizzas.

    Retorna:
        str: La opción seleccionada por el usuario.
    """
    print("Bienvenido a Pizza JAT")
    print("1. Personalizar Pizza")
    print("2. Mostrar Ingredientes Actuales")
    print("3. Estimar Tiempo y Confirmar Orden")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def seleccionar_masa():
    """
    Permite al usuario seleccionar el tipo de masa para la pizza.

    Retorna:
        str: El tipo de masa seleccionada por el usuario.
    """
    print("Selecciona el tipo de masa:")
    masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    opcion = int(input("Selecciona una opción: "))
    return masas[opcion - 1]

def seleccionar_salsa():
    """
    Permite al usuario seleccionar el tipo de salsa para la pizza.

    Retorna:
        str: El tipo de salsa seleccionada por el usuario.
    """
    print("Selecciona el tipo de salsa:")
    salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    opcion = int(input("Selecciona una opción: "))
    return salsas[opcion - 1]

def modificar_ingredientes(ingredientes_actuales):
    """
    Permite al usuario agregar o eliminar ingredientes de la pizza.

    Argumentos:
        ingredientes_actuales (list): Lista de ingredientes actualmente seleccionados.

    Retorna:
        list: Lista actualizada de ingredientes después de las modificaciones.
    """
    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    while True:
        print("1. Agregar Ingrediente")
        print("2. Eliminar Ingrediente")
        print("3. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("Selecciona un ingrediente para agregar:")
            for i, ing in enumerate(ingredientes_disponibles, 1):
                print(f"{i}. {ing}")
            seleccion = int(input("Selecciona una opción: "))
            ingrediente = ingredientes_disponibles[seleccion - 1]
            if ingrediente not in ingredientes_actuales:
                ingredientes_actuales.append(ingrediente)
                print(f"{ingrediente} ha sido agregado.")
            else:
                print(f"{ingrediente} ya está en la pizza.")
        
        elif opcion == "2":
            print("Selecciona un ingrediente para eliminar:")
            for i, ing in enumerate(ingredientes_actuales, 1):
                print(f"{i}. {ing}")
            seleccion = int(input("Selecciona una opción: "))
            ingrediente = ingredientes_actuales.pop(seleccion - 1)
            print(f"{ingrediente} ha sido eliminado.")
        
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    
    return ingredientes_actuales

def mostrar_ingredientes(ingredientes_actuales):
    """
    Muestra los ingredientes actualmente seleccionados para la pizza.

    Argumentos:
        ingredientes_actuales (list): Lista de ingredientes actualmente seleccionados.
    """
    print("Ingredientes actuales en la pizza:")
    for ingrediente in ingredientes_actuales:
        print(f"- {ingrediente}")

def estimar_tiempo(ingredientes_actuales):
    """
    Calcula el tiempo estimado para preparar la pizza en función de los ingredientes seleccionados.

    Argumentos:
        ingredientes_actuales (list): Lista de ingredientes actualmente seleccionados.

    Retorna:
        int: Tiempo estimado en minutos para preparar la pizza.
    """
    tiempo_base = 20
    tiempo_total = tiempo_base + 2 * len(ingredientes_actuales)
    return tiempo_total

def confirmar_orden(tiempo_estimado):
    """
    Permite al usuario confirmar la orden de la pizza después de estimar el tiempo de preparación.

    Argumentos:
        tiempo_estimado (int): Tiempo estimado en minutos para preparar la pizza.
    """
    print(f"El tiempo estimado de preparación es de {tiempo_estimado} minutos.")
    confirmar = input("¿Deseas confirmar la orden? (s/n): ")
    if confirmar.lower() == 's':
        print("¡Orden confirmada! Tu pizza estará lista pronto.")
    else:
        print("Orden cancelada.")

def main():
    """
    Función principal que ejecuta el sistema de personalización de pizzas.
    Permite al usuario personalizar su pizza, mostrar los ingredientes actuales,
    estimar el tiempo de preparación y confirmar la orden.
    """
    masa = "Masa Tradicional"
    salsa = "Salsa de Tomate"
    ingredientes = ["Queso"]
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            masa = seleccionar_masa()
            salsa = seleccionar_salsa()
            ingredientes = modificar_ingredientes(ingredientes)
        
        elif opcion == "2":
            mostrar_ingredientes(ingredientes)
        
        elif opcion == "3":
            tiempo_estimado = estimar_tiempo(ingredientes)
            confirmar_orden(tiempo_estimado)
        
        elif opcion == "4":
            print("Gracias por usar el sistema de Pizza JAT. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
