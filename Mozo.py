class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def obtenerNombre(self) -> str:
        return self.nombre

    def tomarPizzas(self, pizzas: list):
        if len(self.pizzas) + len(pizzas) > 2:
            raise ValueError("El mozo solo puede llevar hasta 2 pizzas")
        self.pizzas.extend(pizzas)

    def servirPizzas(self):
        if self.pizzas:
            print(f"{len(self.pizzas)} pizzas fueron servidas.")
            self.pizzas.clear()
        else:
            print("No hay pizzas para servir.")

    def obtenerPizzas(self) -> list:
        return self.pizzas

    def obtenerEstadoLibre(self) -> bool:
        return len(self.pizzas) < 2
