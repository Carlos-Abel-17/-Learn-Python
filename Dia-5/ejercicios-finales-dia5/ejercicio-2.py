def letras_unicas(palabra):

    mi_set = set()

    for letras in palabra:
        mi_set.add(letras)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas("programacion"))  # Debería devolver ['a', 'c', 'g', 'i', 'm', 'n', 'o', 'p', 'r']