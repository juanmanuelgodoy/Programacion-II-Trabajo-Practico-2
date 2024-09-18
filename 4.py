""" 4. Una vez codificadas en Python las Clases de los puntos anteriores, 
instancie los objetos tal como sucede en las siguientes instrucciones:
mozo1 = Mozo(‘Alfredo’)
mozo2 = Mozo(‘Alfredo’) """

class Mozo():

    nombreMozo = []

    def __init__(self, nombre):
        self.nombre = nombre

    def establecerNombre(self, nombre):
        self.nombre = nombre
        self.nombreMozo.append(nombre)
        print(f"El nombre del mozo es: {self.nombreMozo[0]}")   

mozo1 = Mozo('Alfredo')
mozo2 = Mozo('Alfredo')

print("Ejercicio 4: ")
print("Luego de instanciarse ambos objetos obtenemos: ")
print(f"El nombre del primer mozo es: {mozo1.nombre} y del segundo mozo es: {mozo2.nombre}")

""" Luego, responda lo siguiente:"""
print("i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?") 

print(f"El identificador del primer mozo es: {id(mozo1)} y del segundo mozo es: {id(mozo2)}")

print("No hacen referencia al mismo objeto porque ambos a pesar de ser objetos que se inicializan con el mismo método de la clase Mozo, no tienen la misma posición de memoria (id)")

print("ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.")

def equals(self, mozo):
    return self.nombre == mozo.nombre

print(f"Ambos objetos son equivalentes porque al ejecutar el método equals este nos devuelve: {equals(mozo1, mozo2)}")

print("Por lo tanto ambos objetos comparten el mismo valor de su atributo")

print("iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?")

print(f"Los objetos ligados a mozo1 y mozo2 no comparten la misma posición de memoria porque  cada instancia de una clase tiene su propia dirección en la memoria")
