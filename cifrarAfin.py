import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

M = input("Introduce el mensaje a cifrar: ")
a = int(input("Introduce la constante de decimación: "))
b = int(input("Introduce la constante de desplazamiento: "))
inv = 7 #CAMBIAR CADA VEZ
C = ""

for letra in M:
    if(letra==" "):
            C+=" "
    else:
        op = ((a * alfabeto.index(letra) + b)%27)
        add = alfabeto[op]
        C+=add
        print("Ci = (" + str(a) + "*" + str(alfabeto.index(letra)) + "+" + str(b) + ") mod 27 = " + str(add))
                
print("El mensaje cifrado es: " + C)