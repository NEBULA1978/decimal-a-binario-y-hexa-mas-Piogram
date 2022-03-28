"""
def mensaje():
    print("Bienvenido Ramon")
print("Inicio")
mensaje()
print("Final")

"""

def mensaje(nombre):
    print("Bienvenido Ramon")

def mensaje2(nombre):
    print("Bienvenido",nombre)


def mensaje3(nombre):
    cadena="Bienvenido " + nombre
    return  cadena

def lenN(cadena):
    cont = 0
    for caract in cadena:
        cont += 1
    return cont

def validar_numero(cadena):
    while not cadena.isdigit():
        cadena=input("Error, Ingrese un numero: ")
    return  int(cadena)
