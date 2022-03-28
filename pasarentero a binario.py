#con base a 1byte
# 2 elevado a 8 = 256
print("Convertir un numero Deciml a Binario, Hexadecimal y Octal:")
numero=int(input("Entre un numero Decimal:"))
dec_bin=bin(numero)
print("El equivalente a Binario es:",dec_bin)
dec_hex=hex(numero)
print("El equivalente a Hexadecimal es:", dec_hex)
dec_oct=oct(numero)
print("El equivalente a Octl es:", dec_oct)