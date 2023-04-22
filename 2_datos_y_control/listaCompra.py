lista = []

print("Programa lista de la compra")

while True:
    producto = input("Que desea comprar? (Q para salir): ")
    if producto == "Q":
        break
    elif producto not in lista:
        if input('Seguro que quiere añadir "{}"? [S/N]: '.format(producto)) == "S":
            lista.append(producto)
            print("{} añadido!".format(producto))
    else:
        print("{} ya esta en la lista!".format(producto))

print("La lista de la compra es:\n{}".format(lista))