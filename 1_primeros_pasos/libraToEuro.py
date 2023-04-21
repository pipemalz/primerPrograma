decision = input("¿Qué desea hacer?\n" \
                 " 1. Convertir Dolar a Euro\n" \
                 " 2. Convertir Euro a Dolar\n" \
                 " 3. Convertir Libra a Euro\n" \
                 " 4. Convertir Euro a Libra\n" \
                 "Introduzca el numero de la opcion que desea: ")

libra_euro = 1.13450
libra_dolar = 1.243346
euro_dolar = 1.0959337

if decision == "1":
    dolares = float(input("Introduce la cantidad de Dolares: "))
    euros = dolares / euro_dolar
    print("{} Dolares son {} Euros".format(dolares, euros))
elif decision == "2":
    euros = float(input("Introduce la cantidad de Euros: "))
    dolares = euros * euro_dolar
    print("{} Euros son {} Dolares".format(euros, dolares))
elif decision == "3":
    libras = float(input("Introduce la cantidad de Libras: "))
    euros = libras * libra_euro
    print("{} Libras son {} Euros".format(libras, euros))
elif decision == "4":
    euros = float(input("Introduce la cantidad de Euros: "))
    libras = euros / libra_euro
    print("{} Euros son {} Libras".format(euros, libras))
else:
    print("La opcion seleccionada no existe")
