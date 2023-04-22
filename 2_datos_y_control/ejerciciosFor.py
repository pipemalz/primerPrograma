import string

texto_usuario = input("Escribe un texto para analizarlo: ")
espacios = 0
puntos = 0
comas = 0
mayusculas = 0

for caracter in texto_usuario:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1
    elif caracter in string.ascii_uppercase:
        mayusculas += 1

print("Tu texto contiene:\nEspacios: {}\nPuntos: {}\nComas: {}\nMayusculas: {}".format(espacios, puntos, comas, mayusculas))

