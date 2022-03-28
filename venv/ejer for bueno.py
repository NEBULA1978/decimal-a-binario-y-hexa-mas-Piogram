
"""
frutas=["Mora","Fresa","Mora","Piña","Uva"]
#          0      1       2     3      4
cantidad=[  5 ,   10  ,   3  ,  5   ,  10 ]
clientes=["Axell","Zarinna","Luis","Joel","Kevin"]

#imprimir por pantalla tos las personas que compraron
#MOra y la cantidad

for fruta in frutas:
    pos=frutas.index(fruta)
    if fruta=="Mora":
        can=cantidad[pos]
        cli=clientes[pos]
        print(cli,can)

"""

frutas=["Mora","Fresa","Mora","Piña","Uva"]
#          0      1       2     3      4
cantidad=[  5 ,   10  ,   3  ,  5   ,  10 ]
clientes=["Axell","Zarinna","Luis","Joel","Kevin"]

#imprimir por pantalla todas las personas que compraron
#  Mora y la cantidad

for i in range(len(frutas)):
    fruta=frutas[i]
    if fruta=="Mora":
        can=cantidad[i]
        cli=clientes[i]
        print(cli,can)