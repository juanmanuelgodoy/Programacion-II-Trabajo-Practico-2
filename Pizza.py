class Pizza:
    def __init__(self, var: str):
        self.variedad = var

    def establecerVariedad(self, var: str):
        self.variedad = var

    def obtenerVariedad(self) -> str:
        return self.variedad
# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Ingresar variedad de la pizza")
    print("2. Mostrar variedad de la pizza")
    print("3. Cambiar variedad de la pizza")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            variedad = input("Introduce la variedad de la pizza: ")
            pizza = Pizza(variedad)
            print(f"Pizza de variedad '{pizza.obtenerVariedad()}' creada.")

        case "2":
            if 'pizza' in locals():
                print(f"La variedad de la pizza es: {pizza.obtenerVariedad()}")
            else:
                print("Primero debes ingresar la variedad de la pizza (opción 1).")

        case "3":
            if 'pizza' in locals():
                nueva_variedad = input("Introduce la nueva variedad de la pizza: ")
                pizza.establecerVariedad(nueva_variedad)
                print(f"La nueva variedad de la pizza es: {pizza.obtenerVariedad()}")
            else:
                print("Primero debes ingresar la variedad de la pizza (opción 1).")

        case "4":
            print("Saliendo del menú.")
            break

        case _:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")







