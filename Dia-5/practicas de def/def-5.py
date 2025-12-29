"""
                                        VALIDACION DE LISTA NUMERICA

    la fn es_lista_numerica funcion de validacion recibe un parametro llamado lista verifica que todos los elementos de la
    lista sean numeros int o float debe de devolver true - false si cumple o no

    la fn sumar_lista recibe una lista usa la fn es_lista_numerica si la lista en valida suma todos los valores de la lista
    si no es valida devuelve None (o un valor que tu definas )

    la fn evaluar_lista recibe la lista original llama a sumar_lista si hay suma devuelve un mensaje positivo de lo contrario
    un mensaje de error

"""
lista_a_evaluar = [1, 2, 3, 4, 5, 6, 7, "f", 9, 10]


def es_lista_numerica(lista):
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            return False
    return True


def sumar_lista(lista):
    if not es_lista_numerica(lista):
        return None

    suma = 0
    for elemento in lista:
        suma += elemento

    return suma


def evaluar_lista(lista):
    suma = sumar_lista(lista)

    if suma is None:
        return "No se realizó la suma: la lista contiene valores no numéricos"
    else:
        return f"La suma es {suma}"


print(evaluar_lista(lista_a_evaluar))
