def  analizador_texto(texto):

    texto_list = list(texto)
    unicos = set(texto_list)
    return sorted(unicos)

print(analizador_texto("holaquetal"))  # Debería devolver ['h', 'o', 'l', 'a', ' ', 'q', 'u', 'e', 't']