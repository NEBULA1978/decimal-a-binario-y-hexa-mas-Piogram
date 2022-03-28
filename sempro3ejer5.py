"""
Escriba un programa simulandoel lanzamiento de 3datos,solicite el
montoque desea apostar,si dos numeros son iguales el jugador gana la mitad
de lo que aposto,si los tres numeros son iguales el jugador gana el doble,
caso contrario si los 3numeros son diferentes entonces el jugador pierde
todo lo apostado.
"""
from random import *
apuesta=int(input("Ingrese monto: "))
num1=randint(1,6)
num2=randint(1,6)
num3=randint(1,6)
print(num1,num2,num3)
if (num1==num2 and num2==num3 and num1==num3):
    print("Ganaste el doble")
    apuesta*=2
   #apuesta=apuesta*2
    print("Ahhora tienes: ",apuesta)
elif(num1==num2 or num1==num3 or num2==num3):
    print("Ganaste la mitad de lo apostado")
    mitad= apuesta/2
    apuesta+=mitad
    print("Ahora tienes",apuesta)
else:
    print("Perdiste todo")
