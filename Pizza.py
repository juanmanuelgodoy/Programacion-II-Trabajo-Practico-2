class Pizza():

        variedadPizza = []
        def __init__(self, var=""):
            self.var = var
        
        def establecerVariedad(self, var):
            self.var = var
            self.variedadPizza.append(var)
            print(f"Variedad establecida: {self.variedadPizza[-1]}")

        def obtenerVariedad(self):
            if self.variedadPizza == []: 
                print("No hay ninguna variedad cargada.")
            else:
                for var in self.variedadPizza:
                    print(f"La variedad de la pizza es: {var}")
                

def menuPizza():
    pizza = Pizza()

    while True:
        print("========== Menú Pizza ==========")
        print("1- Establecer variedad")
        print("2- Obtener variedad")
        print("0- Salir del menú Pizza")
        print("===============================")
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Pizza.")
                break

            case 1:
                variedad = input("Ingrese la variedad de la pizza: ")
                pizza.establecerVariedad(variedad)

            case 2:
                pizza.obtenerVariedad()

            case _:
                print("La opción ingresada no es válida, ingrese una opción válida: ")