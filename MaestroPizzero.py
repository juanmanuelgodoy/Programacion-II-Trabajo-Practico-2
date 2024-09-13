import Pizza 
class MaestroPizzero:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPedido(self, var: str):
        if not var:
            raise ValueError("El nombre de la variedad no puede estar vacío")
        pizza = Pizza(var)
        self.pizzasPorCocinar.append(pizza)

    def cocinar(self):
        if self.pizzasPorCocinar:
            self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
            self.pizzasPorCocinar.clear()
            print(f"{len(self.pizzasPorEntregar)} pizzas han sido cocinadas.")
        else:
            print("No hay pizzas para cocinar.")

    def entregar(self) -> list:
        if not self.pizzasPorEntregar:
            return []
        entregadas = self.pizzasPorEntregar[:2]  # Máximo 2 pizzas
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        return entregadas
    
    def obtenerNombre(self) -> str:
        return self.nombre

    def obtenerPizzasPorCocinar(self) -> list:
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self) -> list:
        return self.pizzasPorEntregar  

def maestroPizzero():
    maestro = MaestroPizzero()

    while True:
        print("========== Menú Maestro Pizzero ==========")
        print("1. Establecer nombre")
        print("2. Tomar pedido")
        print("3. Cocinar pizzas")
        print("4. Entregar pizzas")
        print("5. Obtener nombre")
        print("6. Obtener pizzas por cocinar")
        print("7. Obtener pizzas por entregar")
        print("8. Salir del menú Maestro Pizzero")

        opcion = int(input("Seleccione una opcion: "))

        match opcion:
            case 1: 
                nombre = input("Ingrese el nombre del maestro pizzero: ")
                maestro.establecerNombre(nombre)
                print(f"Nombre del maestro establecido: {maestro.obtenerNombre()}")

            case 2:
                pizza = input("Ingrese el nombre de la pizza: ")
                maestro.tomarPedido(pizza)

            case 3:
                maestro.cocinar()

            case 4:
                maestro.entregar()

            case 5:
                print(f" El nombre del maestro pizzero es: {maestro.obtenerNombre()}")

            case 6:
                print(f"Pizzas por cocinar: {maestro.obtenerPizzasPorCocinar()}")

            case 7:
                print(f"Pizzas por entregar: {maestro.obtenerPizzasPorEntregar()}")

            case 8:
                print("Saliendo del menú Maestro Pizzero...")
                break

            case _:
                print("Opción invalida. Intente nuevamente.")
