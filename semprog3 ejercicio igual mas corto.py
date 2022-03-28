
""""
programa de edad e imprime si eres recien nacido ,bebe jove y adulto
"""


#if  Exp booleana :
#   sentencias
edad= int(input("Ingrese su edad: "))
if (edad<=3):
    print("Eres un bebe")
elif (edad<=12):
    print("Eres un niño")
elif(edad<=17):
    print("Eres un joven")
elif(edad==0):
    print("Eres recien nacido")

else:
    print("Eres un adulto")
print("Fin del programa")