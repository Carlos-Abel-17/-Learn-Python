"""Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función
debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el metodo choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
"""
import random


def lanzar_dados():
    dado_uno = random.randint(1, 6)
    dado_dos = random.randint(1, 6)

    datos_dados = [dado_uno, dado_dos]
    return datos_dados

ejecutar_def_uno = lanzar_dados()
result_dado_uno = ejecutar_def_uno[0]
result_dado_dos = ejecutar_def_uno[1]

#print(lanzar_dados())


def evaluar_jugada(dado_uno, dado_dos):
    suma_result = dado_uno + dado_dos

    if suma_result <= 6:
        return f"La suma de tus dados es {suma_result}. Lamentable"

    elif 6 < suma_result < 10:
        return f"La suma de tus dados es {suma_result}. Tienes buenas chances"

    else:
        return f"La suma de tus dados es {suma_result}. Parece una jugada ganadora"


print(evaluar_jugada(result_dado_uno, result_dado_dos))
