"""
ejer2:
Usted cuenta con 3 listas:matriculas ,nombres  promedios

matricula=["201611882","201923457","201957410",....]

nombres=["Villamar Saltos","Concha Regatto","Buestan Villaroel",...]

promedios=[70,80,54,...]

ojo:elestudiante conmatricula 201923457 es Concha Regatto y aprobo con
un promedio de 80

Escriba el programa que permita el ingreso de una matricula.
Elprograma mostrara apellido y el promedio si el estudiante aprobo,
si el estudiante no aprobo el programa mostrara que reprobo la materia.

Ejemplo1:
Ingrese matricula:201923457
Concha Regatto usted aprobo la materia con uun promedio de:80

"""
matricula=["201611882","201923457","201957410"]

nombres=["Villamar Saltos","Concha Regatto","Buestan Villaroel"]

promedios=[78,80,54]
#print(matricula[1],nombres[1],promedios[1])

ingreso=input("Ingrese Matricula: ")#201923457
posMatri=matricula.index(ingreso)# 1 conocer la posicionamtricula
nom=nombres[posMatri]#Concha Regatto
prom=promedios[posMatri]# 80
#print(ingreso, nom, prom)

if (prom >=60):
    print(nom, "usted aprobo la materia con um promedio de:",prom)
else:
    print(nom, "usted reprobo la materia")