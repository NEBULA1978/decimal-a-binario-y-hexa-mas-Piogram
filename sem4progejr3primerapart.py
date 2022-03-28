"""
Ejercicio3

Dada la diguente lista de tweets:

tweet=["@anita123|Lenin Moreno|20/09/2016","@pedro85|Paco Moncayo|15/08/016",
Lasso|25/09/2015",........,"pepe12|Paco Moncayo|10/08/2016","#esyefy1|Lenin
Moreno|25/09/2015"|

Realice un conteo de los votos de cada candidato,

indique a los usuarios que ha emitido mas de 1voto,
y tambien los usuarios que votaron el mismo dia(debe especificar
quienes y en que dia votaron).

NOTA:Tomar en consideracion que la cantidad de candidatos puede variar

"""
tweet=["@anita123|Lenin Moreno|20/09/2016", "@axell|Guillermo Lasso|21/09/2016","@Josue|Guillermo Lasso|19/09/016","@regatto|Lenin Moreno|18/09/2016","@Paulette|Viteri|16/09/2016","@anita123|Lenin Moreno|20/09/2016","@anita123|Lenin Moreno|20/09/2016"]
canditos=[]#["Lenin Moreno","Guillermo Lasso"]
votos=[]#[2,2]
usuarios=[]
fechas=[]
for registro in tweet:#"@anita123|Lenin Moreno|20/09/2016"
    temp=registro.split("|")# ["@anita123","Lenin Moreno"."20/09/2016"]
    cand=temp[1]#"Lenin Moreno"
    if cand not in canditos:
        canditos.append(cand)
        votos.append(1)
    else:
       posCand=canditos.index(cand)
       votos[posCand]+=1
print(canditos)
print(votos)