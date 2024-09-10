import MaestroPizzero
import Mozo
import Pizza

def menu():
    print("====== Pizzería Don Pipo TUDW - FCAD - UNER ========\n")
    print("================ MENÚ GENERAL ======================\n")
    print("Seleccione la opción que desea:  ")
    print("=====================================================")
    print("1- Para pedir una pizza")
    print("2- Para ordenar a la cocina ")
    print("3- Para entregar una pizza")
    print("0- Para salir del menú general")
    print("===================================================\n")


def iniciar():
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case '1':
                Pizza.pizza()  
            case '2':
                MaestroPizzero.maestroPizzero()  
            case '3':
                Mozo.mozo()  
            case '0':
                exit()
            case _:
                print("La opción ingresada no es válida, ingrese una opción válida:")

iniciar()