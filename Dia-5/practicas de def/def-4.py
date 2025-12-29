"""
                Doble resultado juego de dados
    funcion lanzar_dados;simula el lanzamiento de dados para ser exactos de dos dados y debe de devolver una lista con los resultados

    funcion es_doble debe de verificar si los resultados emitidos por la funcion lanzar_dados son iguales y emite un true o false como
    respuesta dependiendo de la comparacion de los resultado.

    funcion evaluar_jugada recibe la lista de los dos resultados y usa la funcion es_doble para verificar la igualdad y devuelve mensajes
    acorde a lo evaluado.
    1.- true: "DOBLE GANADOR"
    2.- false: "SIGUE INTENTANDO"
"""

import random

def lanzar_dados():
    dado_one = random.randint(1, 6)
    dado_two = random.randint(1, 6)
    return  [dado_one, dado_two]

def es_doble(result_dados):

    return  result_dados[0] == result_dados[1]


def evaluar_jugada(result_dados):
    if es_doble(result_dados):
        return "DOBLE GANADOR"
    else: return "SIGUE INTENTANDO"

dados = lanzar_dados()
resultado = evaluar_jugada(dados)

print(f"Dados: {dados}")
print(f"Resultado: {resultado}")
