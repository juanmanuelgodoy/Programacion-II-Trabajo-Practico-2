from Pizza import Pizza
class MaestroPizzero:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def obtenerNombre(self) -> str:
        return self.nombre

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

    def obtenerPizzasPorCocinar(self) -> list:
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self) -> list:
        return self.pizzasPorEntregar
    
# Pedir el nombre del maestro pizzero por input
nombre_pizzero = input("Introduce el nombre del maestro pizzero: ")
maestro = MaestroPizzero(nombre_pizzero)

# Mostrar el nombre del maestro pizzero
print(f"El nombre del maestro pizzero es: {maestro.obtenerNombre()}")

# Cambiar el nombre del maestro pizzero por input
nuevo_nombre = input("Introduce el nuevo nombre del maestro pizzero: ")
maestro.establecerNombre(nuevo_nombre)

# Mostrar el nuevo nombre
print(f"El nuevo nombre del maestro pizzero es: {maestro.obtenerNombre()}")
