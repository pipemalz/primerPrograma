numeros_brutos = input("Introduzca los numeros separados por comas: ")
numeros = [int(numero) for numero in numeros_brutos.split(",")]
numero_pequeno = numeros[0]
numero_grande = numeros[0]

for numero in numeros[1:]:
    if numero < numero_pequeno:
        numero_pequeno = numero
    if numero > numero_grande:
        numero_grande = numero

print("Numeros elegidos: {}\nNumero pequeno: {}\nNumero grande: {}".format(numeros, numero_pequeno, numero_grande))