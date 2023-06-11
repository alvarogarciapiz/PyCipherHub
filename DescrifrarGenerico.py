import numpy as np

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

C = input("Introduce el texto cifrado: ")
B = int(input("Introduce la constante de desplazamiento: "))
M = ""

for letra in C:
    if(letra==" "):
            M+=" "
    else:
        posicionLetraNueva = ((alfabeto.index(letra) + 27 - B) % 27)
        letraNueva = alfabeto[posicionLetraNueva]
        M+=letraNueva
        
                
print("El mensaje descifrado es: " + M)