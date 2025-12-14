##ESCANER DE TEXTO
##  PASOS
##  1.- le debe de pedir al usuario que ingrese un texto
##  2.- luego le pedira que ingrese 3 letras a su elecion
##  PROCESO LOGICO A PLANTEAR
##   1.- Contar cuantas veces aparece cada letra que el eligio(pasar el texto ingresado en minuscula)
##   2.- Contar cuantas palabras hay en total
##   3.- Devolver primera y ultima letra
##   4.- Devolver las palabras en orden inverso
##   5.- Buscar la palabra python

print('PROGRAMA ANALIzADOR DE TEXTO')
## CAPTURA DE DATOS
texto = input('Ingrese un texto:').lower()

print('Ingrese 3 letras para realizar el proceso con el texto')

letras = input('Ingrese las 3 letras:')
letras = letras.replace(' ','').strip().lower()
# print(len(letras))

while len(letras) != 3:
    print('ATENCIÓN: Solo se aceptaran 3 caracteres')
    letras = input('Ingrese las 3 letras:')

letras_separadas = list(letras)
# print(len(letras_separadas))
if len(letras_separadas) != 3:
    letras_separadas = letras.split(' ')

## INICIAR PROCESO

contar_letras_1 = texto.count(letras_separadas[0])
contar_letras_2 = texto.count(letras_separadas[1])
contar_letras_3 = texto.count(letras_separadas[2])

contar_palabras_texto = len(texto.split(' '))

texto_lista = list(texto.strip())
texto_lista_n_reverse = list(texto.strip())

# print(texto_lista.reverse())
texto_lista.reverse()
texto_reverse = "".join(texto_lista)

exite_py = False
if texto.count("python") == 0:
        exite_py = False
else:
        exite_py = True

# SALIDA DE INFORMACION

# Hola como estas que te cuentas
# Hola como estas que te cuentas Python
# a o   e

print(f'la letra {letras_separadas[0]} aparece ->>> {contar_letras_1} veces en todo el texto')
print(f'la letra {letras_separadas[1]} aparece ->>> {contar_letras_2} veces en todo el texto')
print(f'la letra {letras_separadas[2]} aparece ->>> {contar_letras_3} veces en todo el texto')
print(f'Cantidad de palabras en el texto ingresado->>> {contar_palabras_texto}' )
print(f'la primera letra es ->>> {texto_lista_n_reverse[0]} y la ultima letra es ->>> {texto_lista_n_reverse[-1]}')
print(f'el texto reverso ->>> {texto_reverse}')
print(f'La palabra "python" esta en el texto ingresado: {exite_py}')