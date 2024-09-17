import Pizza
import MaestroPizzero

class Mozo():

    nombreMozo1 = []
    nombreMozo2 = []
    def __init__(self, nombre="", pizza=None):
        self.nombre = nombre
        self.pizzas = []

    def establecerNombre1(self, nombre):
        self.nombre = nombre
        self.nombreMozo1.append(nombre)
        print(f"El nombre del primer mozo es: {self.nombreMozo1[-1]}")        

    def establecerNombre2(self, nombre):
        self.nombre = nombre
        self.nombreMozo2.append(nombre)
        print(f"El nombre del segundo mozo es: {self.nombreMozo2[-1]}")        

    def tomarPizzas1(self, pizza):
        self.pizzas.append(pizza)
        print(f"Pedido de {pizza} recibido.")

    def tomarPizzas2(self, pizza):
        self.pizzas.append(pizza)
        print(f"Pedido de {pizza} recibido.")        

    def servirPizzas1(self):
        if len(self.pizzas) > 0:
            pizza = self.pizzas.pop(0)
            print(f"Sirviendo pizza: {pizza}")
        else:
            print("No hay pizzas por cocinar.")

    def servirPizzas2(self):
        if len(self.pizzas) > 0:
            pizza = self.pizzas.pop(0)
            print(f"Sirviendo pizza: {pizza}")
        else:
            print("No hay pizzas por cocinar.")            
    
    def obtenerNombre1(self):
        if self.nombreMozo1 == []:
            print("El primer mozo aún no tiene nombre definido.")
        else:
            print(f"El nombre del primer mozo es: {self.nombreMozo1[-1]}") 

    def obtenerNombre2(self):
        if self.nombreMozo2 == []:
            print("El segundo mozo aún no tiene nombre definido.")
        else:
            print(f"El nombre del segundo mozo es: {self.nombreMozo2[-1]}")             
    
    def obtenerPizzas(self):
        return len(self.pizzas)
    
    def obtenerEstadoLibre1(self):
        if self.obtenerPizzas1() == 0:
            print(f"El mozo {self.obtenerNombre1()} estado libre")
        else:
            print(f"El mozo {self.obtenerNombre1()} tiene {self.obtenerPizzas1()} pizza(s)")
    
    def obtenerEstadoLibre2(self):
        if self.obtenerPizzas2() == 0:
            print(f"El mozo {self.obtenerNombre2()} estado libre")
        else:
            print(f"El mozo {self.obtenerNombre2()} tiene {self.obtenerPizzas2()} pizza(s)")  

def mozo():
    mozo = Mozo()

    while True:
        print("========== Menú Mozo ==========")
        print("1- Establecer nombre mozo 1")
        print("2- Establecer nombre mozo 2")
        print("3- Tomar pizzas mozo 1")
        print("4- Tomar pizzas mozo 2")        
        print("5- Servir pizzas mozo 1")
        print("6- Servir pizzas mozo 2")        
        print("7- Obtener nombre mozo 1")
        print("8- Obtener nombre mozo 2")
        print("9- Obtener estado del mozo 1")
        print("10- Obtener estado del mozo 2")        
        print("0- Salir del menú Mozo")
        print("===============================")
        
        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 0:
                print("Ha salido del menú Mozo.")
                break

            case 1:
                nombre = input("Ingrese el nombre del primer mozo: ")
                mozo.establecerNombre1(nombre)

            case 2:
                nombre = input("Ingrese el nombre del segundo mozo: ")
                mozo.establecerNombre2(nombre)

            case 3:
                pizza = input("Ingrese el nombre de la pizza pedida: ")
                mozo.tomarPizzas1(pizza)

            case 4:
                pizza = input("Ingrese el nombre de la pizza pedida: ")
                mozo.tomarPizzas2(pizza)                

            case 5:
                mozo.servirPizzas1()

            case 6:
                mozo.servirPizzas2()                

            case 7:
                mozo.obtenerNombre1()

            case 8:
                mozo.obtenerNombre2()              

            case 9:
                mozo.obtenerEstadoLibre1()

            case 10:
                mozo.obtenerEstadoLibre2()

            case _:
                print("Opción no válida, ingrese una opción válida: ") 