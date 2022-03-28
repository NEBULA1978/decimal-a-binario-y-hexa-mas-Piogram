
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
cad=input("Ingrese su nombre: ")
mensaje2(cad)

def mensaje3(nombre):
    cadena="Bienvenido " + nombre
    return  cadena
nom=input("Ingrese su nombre:")
cadenaRetorno=mensaje3(nom)
print(cadenaRetorno)