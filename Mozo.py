import Pizza

class Mozo():
    def __init__(self, nombre="", pizza=None):
        self.nombre = nombre
        self.pizzas = []

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def tomarPizzas(self, pizza):
        self.pizzas.append(pizza)
        print(f"Pedido de {pizza} recibido.")

    def servirPizzas(self):
        if len(self.pizzas) > 0:
            pizza = self.pizzas.pop(0)
            print(f"Sirviendo pizza: {pizza}")
        else:
            print("No hay pizzas por cocinar.")
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPizzas(self):
        return len(self.pizzas)
    
    def obtenerEstadoLibre(self):
        return self.obtenerPizzas() == 0

def mozo():
    mozo = Mozo()

    while True:
        print("========== Menú Mozo ==========")
        print("1- Establecer nombre")
        print("2- Tomar pedidos")
        print("3- Servir pizzas")
        print("4- Obtener nombre")
        print("5- Obtener pizzas")
        print("6- Obtener estado del mozo")
        print("0- Salir del menú Mozo")
        print("===============================")
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Mozo.")
                break

            case 1:
                nombre = input("Ingrese el nombre del mozo: ")
                mozo.establecerNombre(nombre)

            case 2:
                pizza = input("Ingrese el nombre de la pizza pedida: ")
                mozo.tomarPizzas(pizza)

            case 3:
                mozo.servirPizzas()

            case 4:
                mozo.obtenerNombre()

            case 5:
                mozo.obtenerPizzas()

            case 6:
                mozo.obtenerEstadoLibre()

            case _:
                print("Opción no válida, ingrese una opción válida: ") 