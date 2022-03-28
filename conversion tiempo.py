
"""
hora=int(hora)
minutos=int(minutos)
segundos=int(segundos)
Escriba un programa quepida porteclado la hora en formato hh:mm:ss y conviertatodoa segundos.

Porejemplo:

ingrese la hora en formato(hh:mm:ss):1:30:50
La hora ingresada tiene 5450 segundos


"""
tiempo=input("Ingresela hora en formato (hh:mm:ss): ")
hora,minutos,segundos=tiempo.split(":")
total=(int(hora) * 3600) + (int(minutos) * 60) + int(segundos)
print("La hora ingresada tiene %d segundos" % total)
