import numpy as np

alfabetoSinClave = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto = []

C = input("Introduce el texto cifrado: ")
P = int(input("Introduce la posición P: "))
K = input("Introuce la clave de cifrado: ")
M = ""

# Primero se rellena el alfabeto
P-=1
for valorClave in K:
    if not valorClave == " ":
        if not(valorClave in alfabeto):
            alfabeto.insert(int(P), valorClave)
            P+=1

for letras in alfabetoSinClave:
    if(P==26):
        P = 0
    if not(letras in alfabeto):
        alfabeto.insert(int(P), letras)
        P+=1
        
# Se cifra con el nuevo alfabeto
for letra in C:
    if(letra==" "):
            M+=" "
    else:
        pos = alfabeto.index(letra)
        letraNueva = alfabetoSinClave[pos]
        M+=letraNueva

print("El mensaje descifrado es: " + M)