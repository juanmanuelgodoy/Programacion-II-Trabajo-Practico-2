from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
class TesterPizzeria:
    def __init__(self):
        self.maestro_pizzero = None
        self.mozo = None
    def menu_principal(self):
        print("Bienvenido a la Pizzería")

        # Registrar el maestro pizzero
        nombre_pizzero = input("Introduce el nombre del maestro pizzero: ")
        self.maestro_pizzero = MaestroPizzero(nombre_pizzero)

        # Registrar el mozo
        nombre_mozo = input("Introduce el nombre del mozo: ")
        self.mozo = Mozo(nombre_mozo)

        while True:
            print("\n--- Menú Principal ---")
            print("1. Menú Maestro Pizzero")
            print("2. Menú Mozo")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_maestro_pizzero()
            elif opcion == "2":
                self.menu_mozo()
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente nuevamente.")
def menu_maestro_pizzero(self):
        while True:
            print("\n--- Menú Maestro Pizzero ---")
            print("1. Registrar nuevo nombre")
            print("2. Tomar pedido de pizza")
            print("3. Cocinar pizzas")
            print("4. Ver pizzas por cocinar")
            print("5. Ver pizzas por entregar")
            print("6. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre del maestro pizzero: ")
                self.maestro_pizzero.establecerNombre(nuevo_nombre)
                print(f"Nombre actualizado a {self.maestro_pizzero.obtenerNombre()}")
            elif opcion == "2":
                variedad = input("Introduce la variedad de la pizza: ")
                self.maestro_pizzero.tomarPedido(variedad)
            elif opcion == "3":
                self.maestro_pizzero.cocinar()
            elif opcion == "4":
                por_cocinar = self.maestro_pizzero.obtenerPizzasPorCocinar()
                if por_cocinar:
                    print(f"Pizzas por cocinar: {por_cocinar}")
                else:
                    print("No hay pizzas por cocinar.")
            elif opcion == "5":
                por_entregar = self.maestro_pizzero.obtenerPizzasPorEntregar()
                if por_entregar:
                    print(f"Pizzas por entregar: {por_entregar}")
                else:
                    print("No hay pizzas por entregar.")
            elif opcion == "6":
                break
            else:
                print("Opción no válida, intente nuevamente.")
def menu_mozo(self):
        while True:
            print("\n--- Menú Mozo ---")
            print("1. Registrar nuevo nombre")
            print("2. Tomar pizzas para entregar")
            print("3. Servir pizzas")
            print("4. Ver estado del mozo")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre del mozo: ")
                self.mozo.establecerNombre(nuevo_nombre)
                print(f"Nombre del mozo actualizado a {self.mozo.obtenerNombre()}")
            elif opcion == "2":
                pizzas_para_entregar = self.maestro_pizzero.obtenerPizzasPorEntregar()
                if pizzas_para_entregar:
                    self.mozo.tomarPizzas(pizzas_para_entregar[:2])  # Máximo de 2 pizzas
                    self.maestro_pizzero.pizzas_por_entregar = self.maestro_pizzero.pizzas_por_entregar[2:]  # Quitar las entregadas
                else:
                    print("No hay pizzas para entregar.")
            elif opcion == "3":
                self.mozo.servirPizzas()
            elif opcion == "4":
                estado_libre = self.mozo.obtenerEstadoLibre()
                if estado_libre:
                    print(f"El mozo {self.mozo.obtenerNombre()} está libre para llevar pizzas.")
                else:
                    print(f"El mozo {self.mozo.obtenerNombre()} está ocupado con pizzas.")
            elif opcion == "5":
                break
            else:
                print("Opción no válida, intente nuevamente.")
# Ejecutar el programa
if __name__ == "__main__":
    tester = TesterPizzeria()
    tester.menu_principal()