num = int(input("Elige un numero para recrear la tabla de multiplicar: "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} x {} = {}".format(num, n, num * n))