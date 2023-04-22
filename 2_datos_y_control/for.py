frase = input("Introduce una frase para contarle las vocales: ")
vocales = ['a', 'e', 'i', 'o', 'u']
n_vocales = 0
for letra in frase.lower():
    if letra in vocales:
        n_vocales += 1

print("La frase '{}' tiene {} vocales".format(frase, n_vocales))