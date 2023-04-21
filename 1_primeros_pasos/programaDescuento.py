edad = int(input("Joven, Señor, Señora, Niño o Niña; Escribame su edad por favor: "))
tipo_carnet = input("Cual es su tipo de carnet? (E para Estudiante, P Pensionista, F Familia Numerosa, N Nada): ")

if (25 <= edad <= 35 and tipo_carnet == "E") or \
    (edad <= 10 and tipo_carnet == "N") or \
    (edad >= 65 and tipo_carnet == "P") or \
    tipo_carnet == "F":
    print("Se te aplica el descuento!")
else:
    print("No se te aplica el descuento")
