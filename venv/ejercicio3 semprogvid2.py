""""

Escriba un programa quepida porteclado la hora en formato hh:mm:ss y conviertatodoa segundos.

Porejemplo:

ingrese la hora en formato(hh:mm:ss):1:30:50
La hora ingresada tiene 5450 segundos


"""
"""
metodo slicing
tiempo=input("Ingresela hora en formato (hh:mm:ss): ")
horas=tiempo[0:2]
minutos=tiempo[3:5]
segundos=tiempo[6:]
print(horas)
print(minutos)
print(segundos)

"""


"""
metodo split es una funcion
"""
tiempo=input("Ingresela hora en formato (hh:mm:ss): ")
hora,minutos,segundos=tiempo.split(":")
lista=tiempo.split(":")
hora= int(lista[0])
minutos= int(lista[1])
segundos= int(lista[2])
print(hora,minutos,segundos)
