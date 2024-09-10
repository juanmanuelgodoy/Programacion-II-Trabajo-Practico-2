class MaestroPizzero:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def tomarPedido(self, pizza):
        self.pizzasPorCocinar.append(pizza)
        print(f"Pedido de {pizza} recibido.")

    def cocinar(self):
        if self.pizzasPorCocinar:
            pizza = self.pizzasPorCocinar.pop(0)
            self.pizzasPorEntregar.append(pizza)
            print(f"La pizza {pizza} ha sido cocinada.")
        else:
            print("No hay pizzas para cocinar.")

    def entregar(self):
        if self.pizzasPorEntregar:
            pizza = self.pizzasPorEntregar.pop(0)
            print(f"La pizza {pizza} ha sido entregada.")
        else:
            print("No hay pizzas para entregar.")

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar


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
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 0:
                print("Ha salido del menú Maestro Pizzero.")
                break
            case 1:
                nombre = input("Ingrese el nombre del maestro pizzero: ")
                maestro.establecerNombre(nombre)
                print(f"Nombre establecido: {maestro.obtenerNombre()}")
            case 2:
                pizza = input("Ingrese el nombre de la pizza: ")
                maestro.tomarPedido(pizza)
            case 3:
                maestro.cocinar()
            case 4:
                maestro.entregar()
            case 5:
                print(f"El nombre del maestro pizzero es: {maestro.obtenerNombre()}")
            case 6:
                print(f"Pizzas por cocinar: {maestro.obtenerPizzasPorCocinar()}")
            case 7:
                print(f"Pizzas por entregar: {maestro.obtenerPizzasPorEntregar()}")
            case _:
                print("Opción no válida, intente nuevamente.")


