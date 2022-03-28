
import random as rd
"""primer metod slicing
moneda=["CARA","CRUZ"]
decision=input("¿Cara o Cruz? ")
pos=rd.randint(0,1)
resultado=moneda[pos]
print("¡El resultado fue %s" % resultado)
"""

"""segundo metodo choice"""

moneda=["CARA","CRUZ"]
decision=input("¿Cara o Cruz? ")
resultado= rd.choice(moneda)
print("¡El resultado fue %s" % resultado)
