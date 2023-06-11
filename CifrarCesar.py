import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

M = input("Introduce el texto a cifrar: ")
X = input("Introduce la constante de desplazamiento: ")
C = ""

for letra in M:
    if(letra==" "):
            C+=" "
    for letraAlfabeto in alfabeto:
        if(letra==letraAlfabeto):
            posicion = alfabeto.index(letra)
            posicion+= int(X)
            if(posicion>26):
                posicion-=27
            letraNueva = alfabeto[posicion]
            C+=letraNueva
                
print("El mensaje cifrado es: " + C)