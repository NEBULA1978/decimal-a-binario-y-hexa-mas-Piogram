ingreso=""
matriculas=[]
kmL=[]
while(ingreso!="fin"):
    ingreso=input("Ingrese matricula, kilometraje: ")
    if ingreso!="fin":
       datos=ingreso.split(",")
       matri=datos[0]
       km=datos[1]
       matriculas.append(matri)
       kmL.append(int(km))
mayorKm=max(kmL)
posKm=kmL.index(mayorKm)
mayorMatri=matriculas[posKm]
print("La matricula con mayor km es: ",mayorMatri,"con:",mayorKm,"km")


