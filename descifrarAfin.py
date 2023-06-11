import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

C = input("Introduce el texto cifrado: ")
a = int(input("Introduce la constante de decimación: "))
b = int(input("Introduce la constante de desplazamiento: "))
inv = 11 #CAMBIAR CADA VEZ
M = ""

for letra in C:
    if(letra==" "):
            M+=" "
    else:
        op = (inv*(27 - b + alfabeto.index(letra)))%27
        add = alfabeto[op]
        M+=add
        #print(str(letra) + " = a-1(Ci+n-b)mod27 = " + str(inv)+ "(" + str(alfabeto.index(letra)) + "+ 27-" + str(b) + ") mod 27 = " + str(add))
                
print("El mensaje descifrado es: " + M)