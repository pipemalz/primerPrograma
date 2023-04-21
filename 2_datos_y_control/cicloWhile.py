respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("Que opcion prefieres [A,B,C]?")

print("Respondiste correctamente! tu respuesta es la " + respuesta)


numero = 20

while numero > 0:
    print("mi numero {} es mayor que 0".format(numero))
    numero -= 1