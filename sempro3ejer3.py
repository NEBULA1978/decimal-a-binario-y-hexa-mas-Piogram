"""
ejercicio3
Escriba un programa que simule un programa"piedra papel tijera vs
la computadora,permita que el usuario ingrese una de las tres opciones
"piedra","papel","tijera",la computadora tomara la opcion alazar,
indique si el usuario gano o perdio

Ejemplo:
¿piedra,papel, o tijera?
computadora saco :Piedra
¡Ganastes¡
"""

import random as rd
usuario=input("¿piedra,papel o tijera? ")
listaOpciones=["piedra","papel","tijera"]
#lo que saca la pc abajo
pos=rd.randint(0,len(listaOpciones)-1)# 0 1 2
pc=listaOpciones[pos]
#pc=rd.choice(listaOpciones)
print("La pc saco:", pc)
if (usuario == pc):
    print("¡EMPATE¡")
elif( (usuario=="piedra" and pc=="tijera") or (usuario=="tijera" and pc=="papel") or (usuario=="papel" and pc=="piedra") ):
    print("¡GANASTES¡")
else:
    print("Lo siento persistes...")
