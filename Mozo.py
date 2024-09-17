import Pizza

class Mozo():

    nombreMozo = []

    def __init__(self, nombre="", pizza=None):
        self.nombre = nombre
        self.pizzas = []

    def establecerNombre(self, nombre):
        self.nombre = nombre
        self.nombreMozo.append(nombre)
        print(f"El nombre del mozo es: {self.nombreMozo[-1]}")        

    def tomarPizzas(self, pizza):
        if len(self.pizzas) < 2:
            self.pizzas.append(pizza)
            print(f'Pedido de una pizza de la variedad: {pizza} recibido')
        else:
            print('El mozo solo puede llevar un máximo de 2 pizzas a la vez.')

    def servirPizzas(self):
        if len(self.pizzas) > 0:
            if len(self.pizzas) == 2: 
                print(f"Sirviendo pizza de la variedad: {self.pizzas[0]} y {self.pizzas[1]}")
                self.pizzas.clear()
            elif len(self.pizzas) == 1:
                print(f"Sirviendo pizza de la variedad: {self.pizzas[0]}")
                self.pizzas.clear()
        else:
            print("No hay pizzas para servir.")

    def obtenerNombre(self):
        if self.nombreMozo == []:
            print("El mozo aún no tiene nombre definido.")
        else:
            print(f"El nombre del mozo es: {self.nombreMozo[-1]}") 

    def obtenerPizzas(self):
        return len(self.pizzas)
    
    def obtenerEstadoLibre(self):
        pizzas = self.obtenerPizzas()  
        nombre = self.obtenerNombre()  

        if pizzas <= 1 and nombre == []:
            print("El mozo aún no tiene nombre definido y está libre.")
        elif pizzas <=1 and nombre != []:
            print("El mozo está libre")
        elif pizzas >2 and nombre == []:
            print(f"El mozo aún no tiene nombre definido y tiene {pizzas} pizza(s) para entregar")
        else:            
            print(f"El mozo tiene {pizzas} pizzas para entregar")

def mozo():
    mozo = Mozo()

    while True:
        print("========== Menú Mozo ==========")
        print("1- Establecer nombre mozo")
        print("2- Tomar pizzas mozo")
        print("3- Servir pizzas mozo")
        print("4- Obtener nombre mozo")
        print("5- Obtener estado del mozo")
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
                pizza = input("Ingrese variedad de la pizza pedida: ")
                mozo.tomarPizzas(pizza)

            case 3:
                mozo.servirPizzas()

            case 4:
                mozo.obtenerNombre()

            case 5:
                mozo.obtenerEstadoLibre()

            case _:
                print("Opción no válida, ingrese una opción válida: ") 