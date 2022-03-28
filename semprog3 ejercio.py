#if  Exp booleana :
#   sentencias
edad= int(input("Ingrse su edad: "))
if (edad>=1 and edad<=3):
    print("Eres un bebe")
elif (edad >=4 and edad<=12):
    print("Eres un niño")
elif(edad >=13 and edad<=17):
    print("Eres un joven")
elif(edad==0):
    print("Eres recien nacido")
else:
    print("Eres un adulto")
print("Fin del programa")