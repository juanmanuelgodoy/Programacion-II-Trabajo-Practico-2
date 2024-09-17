import MaestroPizzero
import Mozo
import Pizza

def menu():
    print("====== Pizzería Don Pipo TUDW - FCAD - UNER ========\n")
    print("================ MENÚ GENERAL ======================\n")
    print("Seleccione la opción que desea:  ")
    print("=====================================================")
    print("1- Menú pizza")
    print("2- Menú maestro pizzero")
    print("3- Menú mozo")
    print("0- Para salir del menú general")
    print("===================================================\n")

def iniciar():
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case '1':
                Pizza.menuPizza()  
            case '2':
                MaestroPizzero.maestroPizzero()  
            case '3':
                Mozo.mozo()  
            case '0':
                exit()
            case _:
                print("La opción ingresada no es válida, ingrese una opción válida:")

if __name__ == '__main__':
    iniciar()