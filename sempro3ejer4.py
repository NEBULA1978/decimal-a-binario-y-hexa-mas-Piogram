"""
ejercicio4
Escriba un programa,que nos permita clasificar un vertebrado o
invertebrado que ingrese el usuario.
Usted cuentacon doslistas llamadas vertebrado y la otra llamada
invertebrado con los nombres de los animales.El programa debe
pedir un animal,y debe decirle al usuariosi lo que ingreso es
un vertebrado o invertebrado:

¿Animal?Ballena
Pertenece a los vertebrado
¿Animal?Camaron
Pertenece a los invertebrados.
"""

vertebrado=["ballena","gato","perro"]
invertebrado=["camaron","medusa","serpiente"]
animal=input("¿Animal? ")
if animal in vertebrado :
    print("Pertenece a los vertebrados")
elif animal in invertebrado:# o con else:
    print("Pertenece alos invertebrados")