'''Crea una función (cantidad_pares) que cuente la
cantidad de números pares que existen en una lista (lista_numeros),
y devuelva el resultado de dicha cuenta.'''


def cantidad_pares(lista_numeros):

    if not isinstance(lista_numeros, list):
        raise TypeError("El parámetro ingresado no es una lista")

    if len(lista_numeros) == 0:
        return 0

    cantidad = 0

    for index, num in enumerate(lista_numeros):

        if not isinstance(num, int):
            raise ValueError(
                f"Elemento no numérico en la posición {index}: {num}"
            )

        if num % 2 == 0:
            cantidad += 1

    return cantidad


lista_numeros = [2, 3, 5, 'f', 6, 8, 3, 5, 2, 4, 67, 54, 90]

try:
    resultado = cantidad_pares(lista_numeros)
    print(resultado)
except (TypeError, ValueError) as error:
    print(error)



