import random

game_over = False
intentos = 3
numero = random.randint(1, 10)

while game_over == False:
    if(intentos == 0):
        game_over = True
        print("Intentos ({})\nPerdiste! El numero ganador era el {}".format(intentos, numero))
    else:
        numero_elegido = int(input("Intentos ({})\nAdivina el numero del 1 al 10: ".format(intentos)))

        if numero_elegido == 666:
            print("Has elegido el numero de la bestia")
        elif numero_elegido > 10:
            print("Te has pasado! Era entre 1 y 10")
        elif numero_elegido < 10:
            print("Te has quedado corto!")

        else:
            if numero_elegido == numero:
                game_over = True
                print("Ganaste!! el numero es {}".format(numero))
            else:
                intentos = intentos - 1
                print("Numero incorrecto!")