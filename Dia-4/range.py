suma_cuadrados = 0

for n in range(1,16):
    cuadrado = n ** 2
    suma_cuadrados = suma_cuadrados + cuadrado
    if n == 15:
        print(suma_cuadrados)