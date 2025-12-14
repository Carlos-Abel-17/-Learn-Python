'''Crea una función (todos_positivos) que reciba una lista de números como parámetro,
y devuelva True si todos los valores de una lista son positivos, y False si al menos
uno de los valores es negativo.
Crea una lista llamada lista_numeros con valores positivos y negativos.

'''

#primera forma mas interactiva, pero sin pensar mucho
'''def detectar_numeros(lista_numeros):
    ''SOLO RECIBE LISTAS''
    iden = type(lista_numeros)
    if iden != list:
        return print('el parametro ingresado no es una lista');

    son_positivos = 0

    for numero in lista_numeros:

        if type(numero) != int:
            return print('uno o mas de valores de la lista no es un numero')

        if numero < 0:
            return print('uno o mas numeros son negativos')
        else:
            son_positivos = 1


    if son_positivos == 1:
        return print('todos los numeros son positivos')
    else:
        return print('todos los numeros son negativos')
'''


#de forma mas simple y corta
'''def todos_positivos(lista_numeros):
    if not isinstance(lista_numeros, list):
        return False

    for numero in lista_numeros:
        if not isinstance(numero, (int, float)) or numero < 0:
            return False

    return True


lista_numeros = [1,2,3,4,5,6,7,8,-9]

print(todos_positivos(lista_numeros))'''


'''detectar_numeros(lista_numeros)'''


#forma mas elaborada y con mas tiempo de analisis
def todos_positivos(lista_numeros):
    """
    Verifica si todos los elementos de una lista son números positivos.

    Parámetros:
        lista_numeros (list): Lista que debe contener números enteros o flotantes.

    Retorna:
        bool: True si todos los números son positivos, False en caso contrario.
    """

    # Validación del tipo de dato
    if not isinstance(lista_numeros, list):
        raise TypeError("El parámetro debe ser una lista")

    # Lista vacía no se considera válida en este contexto
    if len(lista_numeros) == 0:
        return False

    for indice, numero in enumerate(lista_numeros):
        # Validar que cada elemento sea numérico
        if not isinstance(numero, (int, float)):
            raise ValueError(
                f"Elemento inválido en la posición {indice}: {numero}"
            )

        # Validar que sea positivo
        if numero < 0:
            return False

    return True
