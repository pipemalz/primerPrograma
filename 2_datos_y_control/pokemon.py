#import random
from random import randint
import os

VIDA_INICIAL_CPU = 80
VIDA_INICIAL_JUGADOR = 90

TAMANIO_BARRA_VIDA = 50

vida_cpu = VIDA_INICIAL_CPU
vida_jugador = VIDA_INICIAL_JUGADOR

while vida_cpu > 0 and vida_jugador > 0:
    vida_restante_cpu = int((TAMANIO_BARRA_VIDA * vida_cpu) / VIDA_INICIAL_CPU)
    vida_restante_jugador = int((TAMANIO_BARRA_VIDA * vida_jugador) / VIDA_INICIAL_JUGADOR)

    barra_vida_cpu = ("█" * vida_restante_cpu) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_cpu))
    barra_vida_jugador = ("█" * vida_restante_jugador) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_jugador))

    print("\n\nVida Pikachu : {}({}/{})\nVida Squirtle: {}({}/{})".format(barra_vida_cpu, vida_cpu, VIDA_INICIAL_CPU, barra_vida_jugador, vida_jugador, VIDA_INICIAL_JUGADOR))

    #Se desenvuelve los turnos del combate

    #Turno de cpu
    print("\nTurno de Pikachu ")
    ataque_cpu = randint(1, 2)
    if ataque_cpu == 1:
        #Bola Voltio
        print("Pikachu ataca con bola voltio")
        vida_jugador -= 10
    else:
        #Onda trueno
        print("Pikachu ataca con Onda Trueno")
        vida_jugador -= 11

    input("Pulsa enter para continuar...")
    os.system('cls')

    if vida_jugador <= 0:
        vida_jugador = 0
        break

    vida_restante_cpu = int((TAMANIO_BARRA_VIDA * vida_cpu) / VIDA_INICIAL_CPU)
    vida_restante_jugador = int((TAMANIO_BARRA_VIDA * vida_jugador) / VIDA_INICIAL_JUGADOR)

    barra_vida_cpu = ("█" * vida_restante_cpu) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_cpu))
    barra_vida_jugador = ("█" * vida_restante_jugador) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_jugador))

    print("\n\nVida Pikachu : {}({}/{})\nVida Squirtle: {}({}/{})".format(barra_vida_cpu, vida_cpu, VIDA_INICIAL_CPU, barra_vida_jugador, vida_jugador, VIDA_INICIAL_JUGADOR))

    #Turno del Jugador
    print("\nTurno de Squirtle")

    ataque_jugador = None

    while ataque_jugador != "P" and ataque_jugador != "A" and ataque_jugador != "B" and ataque_jugador != "N":
        ataque_jugador = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]o atacar: ")

    if ataque_jugador == "P":
        print("Atacas con Placaje\n")
        vida_cpu -= 10
    elif ataque_jugador == "A":
        print("Atacas con Pistola de Agua\n")
        vida_cpu -= 12
    elif ataque_jugador == "B":
        print("Atacas con Burbuja\n")
        vida_cpu -= 9
    elif ataque_jugador == "N":
        print("No atacas\n")
        vida_cpu -= 0

    if vida_cpu < 0:
        vida_cpu = 0

    input("Pulsa enter para continuar...")
    os.system('cls')

vida_restante_cpu = int((TAMANIO_BARRA_VIDA * vida_cpu) / VIDA_INICIAL_CPU)
vida_restante_jugador = int((TAMANIO_BARRA_VIDA * vida_jugador) / VIDA_INICIAL_JUGADOR)

barra_vida_cpu = ("█" * vida_restante_cpu) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_cpu))
barra_vida_jugador = ("█" * vida_restante_jugador) + ("▒" * (TAMANIO_BARRA_VIDA - vida_restante_jugador))

print("\nVida Pikachu : {}({}/{})\nVida Squirtle: {}({}/{})".format(barra_vida_cpu, vida_cpu, VIDA_INICIAL_CPU, barra_vida_jugador, vida_jugador, VIDA_INICIAL_JUGADOR))

if vida_cpu > vida_jugador:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")