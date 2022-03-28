"""
1tabla de multiplicar introducir un numero

#n=int(input("Ingrese un numero: "))
for n in range(1,11):
    print("---Tabla "+str(n)+"---")# ---Tabla 6---
    for i in range(11):#para todas las tablas del 1 al 10
        resultado= i*n
        print(i,"x",n,"=",resultado)

"""
"""
cadena="Piogram"
#for variable in cadena:
for caracter in cadena:
#    print("Hola")
#    print(variable)
    print(caracter)
"""

"""
ingresar palabra y ver si contienen vocales le diga yo

cadena=input("Ingrese palabra: ").lower()
for caracter in cadena:
    if caracter in "aeoáéó":
        print(caracter)
"""
lista=["Axell","Piogram","youtube","Python"]
for cadena in lista:
    print("----"+cadena+"----")
    for caracter in cadena:
        mini=caracter.lower()
        if mini in "aeoáéó":
            print(mini)

print("Fin del programa")