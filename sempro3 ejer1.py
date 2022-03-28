"""
Escriba  un programa de python que determina si una matricula
de novato es valida.Para que la matricvula sea valida
debe cumplir los siguientes requisitos:
Ejemplo1:
Ingrese la Matricula:201611882
La matricula 301611882 no es valida
Ejemplo2:
Ingrese la Matricula:201923457
La matricula 201923457 es valida
Ejemplo3:
Ingrese la Matricula:2019ABC454
La matricula 2019ABC454 no es valida
"""
"""
matricula=input("Ingrese una matricula: ")
if (matricula[:4]=="2019" and len(matricula)==9 and matricula.isdigit() ):
#if (matricula.startwich("2019")) es lo mismo anterior
   print("La matricula",matricula,"es valida")
else:
   print("La matricula",matricula,"no es valida")
"""
"""
es lo mismo anterior lo de abajo pero con variables
"""

matricula=input("Ingrese una matricula: ")
cond1= matricula[:4]=="2019"#cond1= matricula.startswith("2019) lo mismo
cond2= len(matricula)==9
cond3= matricula.isdigit()

if ( cond1 and cond2 and cond3):
   print("La matricula",matricula,"es valida")
else:
   print("La matricula",matricula,"no es valida")