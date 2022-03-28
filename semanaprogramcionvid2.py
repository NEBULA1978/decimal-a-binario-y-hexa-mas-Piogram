"""
ejer2
Usted quiere empezar a desarrollar un juego que mezcle palabras.
Para empezar debe crear un programa que mezcle las dos palabras
dela siguiente manera:Para cada palbra se debe elegir una letra
al azar y a partir de estaletra y las siguientesse utilizan para
la mezcla.

tres maneras importar
import random
valor=random.randint(4)

import random as rd
valor=rd.randint(4)

Hola
0123
"""
from random import *
"""
palabra1=input("Ingrese palabra 1: ")

pos1=randint(0,len(palabra1)-1)#0123
letra1= palabra1[pos1]
#print("posicion: ",pos)
#print("letra es: ",letra)
print("Letraalazar:",letra1)
resultado1=palabra1[pos1:]
print("Resultado 1:" ,resultado1)

"""

"""
segundo metodo chice 
palabra1=input("Ingrese palabra1: ")

letra=choice(palabra1)
print(letra)
"""

#primer metodo:

palabra1=input("Ingrese palabra 1: ")

pos1=randint(0,len(palabra1)-1)#0123
letra1= palabra1[pos1]
#print("posicion: ",pos)
#print("letra es: ",letra)
print("Letraalazar:",letra1)
resultado1=palabra1[pos1:]
print("Resultado 1:" ,resultado1)
palabra2=input("Ingrese palabra 2: ")
pos2=randint(0,len(palabra2)-1)# 0 1 2 3
letra2= palabra2[pos2]
print("Letra al azar:",letra2)
resultado2=palabra2[pos2:]
print("Resultado 2:",resultado2)
#--------------------------
total=resultado1+resultado2
print("Mezcla:",total)