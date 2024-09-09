from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
class TesterPizzeria:
    def main(self):
        # Crear un único MaestroPizzero
        maestro = MaestroPizzero("Don Pipo")
        
        # Crear dos mozos
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Carlos")

        while True:
            print("\n--- Menú de la Pizzería ---")
            print("1. Tomar pedido")
            print("2. Cocinar pizzas")
            print("3. Entregar pizzas a mozo 1")
            print("4. Entregar pizzas a mozo 2")
            print("5. Mozo 1 sirve pizzas")
            print("6. Mozo 2 sirve pizzas")
            print("7. Ver estado de los mozos")
            print("8. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                variedad = input("Ingrese la variedad de pizza: ")
                maestro.tomarPedido(variedad)
                print(f"Pedido de {variedad} recibido.")
            elif opcion == "2":
                maestro.cocinar()
            elif opcion == "3":
                pizzasParaMozo1 = maestro.entregar()
                try:
                    mozo1.tomarPizzas(pizzasParaMozo1)
                    print(f"Mozo {mozo1.obtenerNombre()} tomó las pizzas.")
                except ValueError as e:
                    print(e)
            elif opcion == "4":
                pizzasParaMozo2 = maestro.entregar()
                try:
                    mozo2.tomarPizzas(pizzasParaMozo2)
                    print(f"Mozo {mozo2.obtenerNombre()} tomó las pizzas.")
                except ValueError as e:
                    print(e)
            elif opcion == "5":
                mozo1.servirPizzas()
            elif opcion == "6":
                mozo2.servirPizzas()
            elif opcion == "7":
                print(f"El mozo {mozo1.obtenerNombre()} está libre: {mozo1.obtenerEstadoLibre()}")
                print(f"El mozo {mozo2.obtenerNombre()} está libre: {mozo2.obtenerEstadoLibre()}")
            elif opcion == "8":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
