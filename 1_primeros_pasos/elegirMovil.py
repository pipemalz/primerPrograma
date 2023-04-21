#iPhone Ultra Pro Max
#iPhone Segunda Mano
#Android Chino 300.000 pesos
#Google Pixel Supercamara
#Android Calidad-Precio
titulo = "A continuacion te ayudare a elegir tu movil nuevo."

print(titulo + "\n" + ("-" * len(titulo)) + "\n")

so = input("Que prefieres?\n1. Android\n2. iOs\nEscribe tu respuesta: ")

money = input("\nTienes dinero?\n1. Si\n2. No\nEscribe tu respuesta: ")

if so == "1":
    if money == "1":
        camara = input("\nTe importa la camara del movil?\n1. Si\n2. No\nEscribe tu respuesta: ")
        if camara == "1":
            print("Google Pixel Supercamara")
        else:
            print("Android Calidad-Precio")
    else:
        print("Android Chino 300.000 pesos")

if so == "2":
    if money == "1":
        print("iPhone Ultra Pro Max")
    else:
        print("iPhone Segunda Mano")
