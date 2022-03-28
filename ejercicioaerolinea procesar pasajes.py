"""

Considere que usted trabaja en una aerolinea, y sele ha encargado la tarea de
procesar los pasajes.Su programa elpasaje en lossiguientes formatos

    Klm7882  navas,cARlos   guayaquil-madrid-guayaquil  20180516  16:30

Lascolumnas debenestar separadas por un espacio Su programa debe pedir un
string con dicho formato y mostrarnos la informacion desglosada.Note que los
datos pueden estar en mayusculas o en minusculas mezcladas
"""





datos=input("Ingrese el pasaje: ")
#"K1m7882 navas,cARlos guayaquil-madrid-guayaquil 20180516 16:30"
pasajeL=datos.split(" ")
#"Klm7882 navas,cARlos guayaquil-madrid-guayaquil 20180516 16:30"

#aerolinea= pasajeL[0][:3]#Klm
aerolinea= pasajeL[0][:-4].upper()#LATAM7882
vuelo=pasajeL[0][-4:]#"7882"
apellido,nombre=pasajeL[1].split(",")#navas,cARlos
pasajero= apellido.title() + " " + apellido.title() #"Carlos" + " " + Navas"
ruta=pasajero[2].replace("-"," ").title().replace(" ","-") #guayaquil-madrid-guayaquil
fecha=pasajeL[3]# "20180516" = "2018-05-16"
fechaFinal= fecha[:4] + "-" + fecha[4:6] + "-" + fecha[-2:]
hora=pasajeL[-1]
print("Aerolinea:",aerolinea)
print("Vuelo:",vuelo)
print("Pasajero:",pasajero)
print("Ruta:",ruta)
print("Fecha:",fechaFinal)
print("Hora:",hora)
