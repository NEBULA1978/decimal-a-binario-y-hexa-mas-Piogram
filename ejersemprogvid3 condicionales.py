

"""
igual que el anterior

edad=int(input("Ingrese su edad: "))
if (edad>=1):
    print("Eres un bebe")
elif (edad >=4):
    print("Eres un niño")
elif (edad >=13):
    print("Eres un joven")
else:
    print("Eres un adulto")

print("Fin del programa")

"""


edad=int(input("Ingrese su edad: "))
if (edad>=1 and edad<=3):
    print("Eres un bebe")
elif (edad >=4 and edad<=12):
    print("Eres un niño")
elif (edad >=13 and edad <=17):
    print("Eres un joven")
else:
    print("Eres un adulto")

print("Fin del programa")