class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def obtenerNombre(self) -> str:
        return self.nombre

    def tomarPizzas(self, pizzas: list):
        if len(self.pizzas) + len(pizzas) > 2:
            raise ValueError("El mozo solo puede llevar hasta 2 pizzas")
        self.pizzas.extend(pizzas)

    def servirPizzas(self):
        if self.pizzas:
            print(f"{len(self.pizzas)} pizzas fueron servidas.")
            self.pizzas.clear()
        else:
            print("No hay pizzas para servir.")

    def obtenerPizzas(self) -> list:
        return self.pizzas

    def obtenerEstadoLibre(self) -> bool:
        return len(self.pizzas) < 2

# Pedir el nombre del mozo por input
nombre_mozo = input("Introduce el nombre del mozo: ")
mozo = Mozo(nombre_mozo)

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Ingresar nombre del mozo")
    print("2. Mostrar nombre del mozo")
    print("3. Cambiar nombre del mozo")
    print("4. Tomar pizzas")
    print("5. Servir pizzas")
    print("6. Ver pizzas en posesión del mozo")
    print("7. Ver si el mozo está libre")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombre_mozo = input("Introduce el nombre del mozo: ")
            mozo = Mozo(nombre_mozo)
            print(f"Mozo {mozo.obtenerNombre()} creado.")

        case "2":
            if 'mozo' in locals():
                print(f"El nombre del mozo es: {mozo.obtenerNombre()}")
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "3":
            if 'mozo' in locals():
                nuevo_nombre = input("Introduce el nuevo nombre del mozo: ")
                mozo.establecerNombre(nuevo_nombre)
                print(f"El nuevo nombre del mozo es: {mozo.obtenerNombre()}")
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "4":
            if 'mozo' in locals():
                try:
                    cantidad = int(input("¿Cuántas pizzas quieres que tome el mozo (máximo 2)? "))
                    if cantidad < 1 or cantidad > 2:
                        print("Error: El mozo puede tomar entre 1 y 2 pizzas.")
                    else:
                        pizzas = [f"Pizza {i+1}" for i in range(cantidad)]
                        mozo.tomarPizzas(pizzas)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "5":
            if 'mozo' in locals():
                mozo.servirPizzas()
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "6":
            if 'mozo' in locals():
                pizzas = mozo.obtenerPizzas()
                if pizzas:
                    print(f"El mozo tiene las siguientes pizzas: {[pizza for pizza in pizzas]}")
                else:
                    print("El mozo no tiene pizzas en este momento.")
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "7":
            if 'mozo' in locals():
                estado = "libre" if mozo.obtenerEstadoLibre() else "ocupado"
                print(f"El mozo está {estado}.")
            else:
                print("Primero debes ingresar el nombre del mozo (opción 1).")

        case "8":
            print("Saliendo del menú.")
            break

        case _:
            print("Opción no válida. Por favor, elige una opción del 1 al 8.")