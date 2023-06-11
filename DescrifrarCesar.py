import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

C = input("Introduce el texto cifrado: ")
X = input("Introduce la constante de desplazamiento: ")
M = ""

for letra in C:
    if(letra==" "):
            M+=" "
    for letraAlfabeto in alfabeto:
        if(letra==letraAlfabeto):
            posicion = alfabeto.index(letra)
            posicion-= int(X)
            if(posicion>26):
                posicion-=27
            letraNueva = alfabeto[posicion]
            M+=letraNueva
                
print("El mensaje descifrado es: " + M)