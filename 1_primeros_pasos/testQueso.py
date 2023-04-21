titulo = "Bienvenido al test de quesudos"
print("\n" + titulo + "\n" + ("-" * len(titulo)) + "\n")

puntuacion = 0

opcion = input("\n¿Con qué frecuencia haces ejercicio?\n"
                "A. Nunca o casi nunca\n"
                "B. De vez en cuando, una vez a la semana\n"
                "C. Regularmente, al menos tres veces a la semana\n"
                "Escribe tu respuesta: ")

if opcion == "A":
    puntuacion += 1
if opcion == "B":
    puntuacion += 2
if opcion == "C":
    puntuacion += 3

opcion = input("\n¿Cuántas horas al día duermes en promedio?\n"
                "A. Menos de 6 horas\n"
                "B. Entre 6 y 8 horas\n"
                "C. Más de 8 horas\n"
                "Escribe tu respuesta: ")

if opcion == "A":
    puntuacion += 1
if opcion == "B":
    puntuacion += 2
if opcion == "C":
    puntuacion += 3

opcion = input("\n¿Cuál es tu nivel de estrés?\n"
                "A. Alto, siento que me afecta en mi vida diaria\n"
                "B. Moderado, a veces me siento estresado pero puedo manejarlo\n"
                "C. Bajo, generalmente me siento tranquilo y relajado\n"
                "Escribe tu respuesta: ")

if opcion == "A":
    puntuacion += 1
if opcion == "B":
    puntuacion += 2
if opcion == "C":
    puntuacion += 3

if 3 <= puntuacion <= 4:
    print("\nTu estado físico puede mejorar.\nTe recomendamos buscar una rutina de ejercicio y establecer un horario de sueño regular.\n")

if 5 <= puntuacion <= 6:
    print("\nTu estado físico es aceptable pero podrías mejorar.\nTe recomendamos seguir haciendo ejercicio regularmente y manteniendo un horario de sueño adecuado.\n")

if 7 <= puntuacion <= 9:
    print("\nTu estado físico es óptimo.\nFelicidades, sigue manteniendo tu rutina de ejercicio y tu horario de sueño regular para mantener tu buena salud física.\n")