import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabetoClave = []

M = input("Introduce el texto a cifrar: ")
clave = input("Introduce la clave: ")
cont = 0
C = ""

#Primero se rellena el alfabetoClave
while cont < len(M):
    i = 0
    for i in clave:
        alfabetoClave.append(i)
        cont+=1

#Se descifra el mensaje
cont = 0
for i in M:
    # i es la letra no la posición
    Ci = alfabeto.index(i)
    Ki = alfabeto.index(alfabetoClave[cont])
    
    op = (Ci + Ki)%27
    add = alfabeto[op]
    C+=add
    cont+=1
    print("Ci = (" + str(Ci) + " + " + str(Ki) + ")mod27 = " + str(add))
                
print("El mensaje cifrado es: " + C)