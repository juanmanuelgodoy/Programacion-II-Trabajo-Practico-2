class Pizza():

        def __init__(self, var=""):
            self.var = var
        
        def establecerNombre(self, var):
            self.var = var
            print(f"Nombre establecido: {pizza.obtenerNombre()}")

        def obtenerVariedad(self):
            return self.var
        print(f"La variedad de la pizza es: {pizza.obtenerVariedad()}")        

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
        print("0- Salir del menú Pizza")
        print("===============================")
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Pizza.")
                break

            case 1:
                nombre = input("Ingrese el nombre de la pizza: ")
                pizza.establecerNombre(nombre)

            case 2:
                pizza.obtenerVariedad()

            case _:
                print("Opción no válida, intente nuevamente.")