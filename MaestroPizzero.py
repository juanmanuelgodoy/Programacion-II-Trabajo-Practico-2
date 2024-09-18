class MaestroPizzero:

    nombreMaestro = []
    pizzasPorEntregar = []

    def __init__(self, nombre=""):
        self.nombre = nombre
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nombre):
        self.nombre = nombre
        self.nombreMaestro.append(nombre)
        print(f"El nombre del maestro pizzero es: {self.nombreMaestro[-1]}")

    def tomarPedido(self, pizza):
        self.pizzasPorCocinar.append(pizza)
        print(f"Pedido de una pizza de la variedad {pizza} recibido.")

    def cocinar(self):

        if len(self.pizzasPorCocinar) != 0:
            for pizza in self.pizzasPorCocinar[:]:
                self.pizzasPorEntregar.append(pizza)
                print(f"La pizza de la variedad {pizza} ha sido cocinada.")

            self.pizzasPorCocinar.clear() 
        else:
            print("No hay pizzas para cocinar.")            




    def entregar(self):

        if len(self.pizzasPorEntregar) > 0:
            if len(self.pizzasPorEntregar) >= 2: 
                print(f"Entregando pizza de la variedad: {self.pizzasPorEntregar[0]} y {self.pizzasPorEntregar[1]}")
                self.pizzasPorEntregar.pop(0)
                self.pizzasPorEntregar.pop(0)
            elif len(self.pizzasPorEntregar) == 1:
                print(f"Entregando pizza de la variedad: {self.pizzasPorEntregar[0]}")
                self.pizzasPorEntregar.pop(0)
        else:
            print("No hay pizzas para entregar.")

    def obtenerNombre(self):
        if self.nombreMaestro == []:
            print("El maestro pizzero aún no tiene nombre definido.")
        else:
            print(f"El nombre del maestro pizzero es {self.nombreMaestro[-1]}") 

    def obtenerPizzasPorCocinar(self):
        if self.pizzasPorCocinar == []: 
            print("No hay ninguna pizza para cocinar")
        else:
            for var in self.pizzasPorCocinar:
                print(f"La pizza por cocinar es de la variedad: {var}")

    def obtenerPizzasPorEntregar(self):
        if self.pizzasPorEntregar == []: 
            print("No hay ninguna pizza para entregar")
        else:
            for var in self.pizzasPorEntregar:
                print(f"La pizza para entregar es de la variedad: {var}")


def maestroPizzero():
    maestro = MaestroPizzero()

    while True:
        print("========== Menú Maestro Pizzero ==========")
        print("1- Establecer nombre")
        print("2- Tomar pedido")
        print("3- Cocinar pizza")
        print("4- Entregar pizza")
        print("5- Obtener nombre")
        print("6- Obtener pizzas por cocinar")
        print("7- Obtener pizzas por entregar")
        print("0- Salir del menú Maestro Pizzero")
        print("=========================================\n")
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Maestro Pizzero.")
                break

            case 1:
                nombre = input("Ingrese el nombre del maestro pizzero: ")
                maestro.establecerNombre(nombre)

            case 2:
                pizza = input("Ingrese el nombre de la pizza: ")
                maestro.tomarPedido(pizza)

            case 3:
                maestro.cocinar()

            case 4:
                maestro.entregar()

            case 5:
                maestro.obtenerNombre()

            case 6:
                maestro.obtenerPizzasPorCocinar()

            case 7:
                maestro.obtenerPizzasPorEntregar()

            case _:
                print("La opción ingresada no es válida, ingrese una opción válida: ")


