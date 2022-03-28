
import random
premios=["lapiz","computadora","carro","pluma","televisor"]
aleatorio=random.choice(premios)
print(aleatorio)
ingreso=input("Ingrese un prenio: ")
cond= aleatorio == ingreso
print("¿Gano?",cond)
