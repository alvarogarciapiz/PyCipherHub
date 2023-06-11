string = input("Ingresa el texto original: ")
caracter = input("Ingresa el carácter a buscar: ")
reemplazo = input("Ingresa el carácter de reemplazo: ")

# Recorre el string y sustituye el caracter
nuevo_string = ""
for i in range(len(string)):
    if string[i] == caracter:
        nuevo_string += reemplazo
    else:
        nuevo_string += string[i]

print(nuevo_string)
