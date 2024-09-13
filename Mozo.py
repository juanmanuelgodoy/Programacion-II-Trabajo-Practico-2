import Pizza

class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPizzas(self, pizzas: list):
        if len(self.pizzas) + len(pizzas) > 2:
            raise ValueError("El mozo solo puede llevar hasta 2 pizzas")
        self.pizzas.extend(pizzas)

    def servirPizzas(self):
        if len(self.pizzas) > 0:
            pizza = self.pizzas.pop(0)
            print("Sirviendo pizza: {pizza}")
        else:
            print("No hay pizzas por cocinar.")
       
    def obtenerNombre(self) -> str:
        return self.nombre
    
    def obtenerPizzas(self) -> list:
        return self.pizzas

    def obtenerEstadoLibre(self) -> bool:
        return len(self.pizzas) == 0 
    
    def mozo():
        mozo = Mozo()

        while True:
            print("========== Menú Mozo ==========")
            print("1. Establecer nombre")
            print("2. Tomar pizzas")
            print("3. Servir pizza")
            print("4. Obtener nombre")
            print("5. Obtener pizzas")
            print("6. Obtener estado libre del mozo")
            print("7. Salir del menú Mozo")
            print("================================")

            opcion = int(input("Ingrese una opción: "))

            match opcion:

                case 1:
                    nombre = input("Ingrese el nombre del mozo: ")
                    mozo.establecerNombre(nombre)
                    print(f"Nombre del mozo establecido: {nombre}")
                
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

                case 7:
                    print("Saliendo del menú Mozo...")
                    break

                case _:
                    print("Opción inválida. Intente nuevamente.")