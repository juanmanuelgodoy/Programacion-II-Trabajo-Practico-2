class Pizza:

    def __init__(self, var: str):
        self.variedad = var

    def establecerVariedad(self, var: str):
        self.variedad = var
        print(f"Nombre establecido: {pizza.obtenernombre(self.variedad)}")

    def obtenerVariedad(self) -> str:
        return self.variedad
        print(f"La variedad de la pizza es: {pizza.obtenervariedad(self.variedad)}")

def pizza():
    pizza = Pizza()

    while True:
        print("========== Menú Pizza ==========")
        print("1- Establecer nombre")
        print("2- Tomar pedido")
        print("3- Cocinar pizza")
        print("4- Entregar pizza")
        print("5- Obtener nombre")
        print("6- Obtener pizzas por cocinar")
        print("7- Obtener pizzas por entregar")
        print("o- Salir del menú Pizza")
        print("================================")

        opcion = int(input("Ingrese una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Pizza.")
                break 

            case 1:
                nombre = input("Ingrese el nombre de la pizza: ")
                pizza.establecerNombre(nombre)
                print("Nombre de la pizza registrado con éxito.")

            case 2: 
                pizza.obtenerVariedad()
                print("Pedido realizado con éxito.")

            case _:
                print("Opción no válida. Intente nuevamente.")