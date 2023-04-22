import string

numeros = []
while True:
    num_usuario = input('Agrega un numero: (Q para salir)')
    es_numero = True
    if num_usuario == 'Q':
        break
    else:
        for caracter in num_usuario:
            if caracter not in string.digits:
                es_numero = False
                print("No es un numero valido")
                break
        if es_numero:
            numeros.append(int(num_usuario))

print("Numeros elegidos:\n{}\nNumero mas pequenio: {}\nNumero mas grande: {}".format(numeros, min(numeros), max(numeros)))
