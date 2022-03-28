"""
ejercicio2
Escribir un programa que permita al usuario el ingreso de n numeros.
Primero debe preguntar alusuario cuantos numero quiere ingresar.
Al final del program presente la sumatoria de dichos numeros.
"""
cuantos=int(input("¿Cuantos numeros desea ingresar? "))
ciclo=0
while ciclo< cuantos:
    num=int(input("Ingrese un numero: "))
    ciclo+= num
    num = int(input("Ingrese un numero: "))
    ciclo==1
print("Total:",num+ciclo)
opcion=""
while opcion!=3:
    cuantos = int(input("¿Que numero desea ingresar? "))
    print("El numero es: ",cuantos)
    ciclo = 0
    print("Bienvenidos a su calculadora")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicar")
    print("4.-Salir")
    opcion=input("Ingrese una opcion: ")
    if(opcion=="1"):
        n1=int(input("Ingrese numero 1: "))
        n2 = int(input("Ingrese numero 2: "))
        total=n1+n2
        print("La suma de todos los numeros es:",total)
    elif (opcion=="2"):
        n1 = int(input("Ingrese numero 1: "))
        n2 = int(input("Ingrese numero 2: "))
        total= n1-n2
        print("La resta de todos los numeros es:",total)
    elif (opcion == "3"):
        n1 = int(input("Ingrese numero 1: "))
        n2 = int(input("Ingrese numero 2: "))
        total = n1 * n2
        print("La multiplicacion de todos los numeros es:", total)
    elif(opcion=="4"):
                    print("Gracias por utilizasr tu calculadora")