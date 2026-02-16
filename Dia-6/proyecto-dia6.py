import os
from pathlib import Path
from os import system

from semilla import crear_estructura_inicial

mi_ruta = Path(Path.home(), "Recetas")

# Crear la carpeta Recetas si no existe
if not mi_ruta.exists():
    mi_ruta.mkdir(parents=True, exist_ok=True)


def contador_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador


def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + 'BIENVENIDO AL SISTEMA DE RECETAS' + '*' * 50)
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Total recetas: {contador_recetas(mi_ruta)}')

    eleccion_menu = 'X'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion:')
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        ''')
        eleccion_menu = input()

    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print('Categorias:')
    ruta_categorias = Path(ruta)
    listar_categorias = []
    contador = 1
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}]- {carpeta_str}')
        listar_categorias.append(carpeta_str)
        contador += 1
    return listar_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'X'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nelegir categoria:')
    
    return  lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print('Recetas:')
    ruta_recetas = Path(mi_ruta, ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}]- {receta_str}')
        lista_recetas.append(receta_str)
        contador += 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = 'X'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\nelegir receta:')
    
    return  lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print('Elija el nombre de la receta:')
        nombre_receta = input() + '.txt'
        print(f'Escribe tu nueva receta:')
        contenido_receta = input()

        ruta_nueva = Path(mi_ruta, ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada exitosamente')
            existe = True
        else:
            print('La receta ya existe')

def crear_categoria(ruta):
    existe = False

    while not existe:
        print('Elija el nombre de la categoria:')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu categoria {nombre_categoria} ha sido creada exitosamente')
            existe = True
        else:
            print('La categoria ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'Tu receta {receta} ha sido eliminada exitosamente')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'Tu categoria {categoria} ha sido eliminada exitosamente')

def volver_inicio():
    eleccion_regresar = 'X'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresiona v para volver al inicio: ')


# Verificar si la estructura inicial existe, si no, crearla
categorias_esperadas = ["Carnes", "Ensaladas", "Pastas", "Postres"]
estructura_existe = all(Path(mi_ruta, cat).exists() for cat in categorias_esperadas)

if not estructura_existe or contador_recetas(mi_ruta) == 0:
    print("Creando estructura inicial de recetas...\n")
    crear_estructura_inicial(mi_ruta)
    print("\n" + "="*50 + "\n")

#Mostrar menu de inicio
finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    if menu == 1:
    #LEER UNA RECETA 
        mis_categorias = mostrar_categorias(mi_ruta)
        la_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(la_categoria)
        mi_receta = elegir_receta(mis_recetas)
        ruta_completa_receta = Path(mi_ruta, la_categoria, mi_receta)
        leer_receta(ruta_completa_receta)
        volver_inicio()
    elif menu == 2:
    #CREAR UNA RECETA 
        mis_categorias = mostrar_categorias(mi_ruta)
        la_categoria = elegir_categoria(mis_categorias)
        crear_receta(la_categoria)
        volver_inicio()
    elif menu == 3:
    #CREAR CATEGORIA
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 4:
    #ELIMINAR UNA RECETA
        mis_categorias = mostrar_categorias(mi_ruta) 
        la_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(la_categoria)
        mi_receta = elegir_receta(mis_recetas)
        ruta_completa_receta = Path(mi_ruta, la_categoria, mi_receta)
        eliminar_receta(ruta_completa_receta)
        volver_inicio()
    elif menu == 5:
    #ELIMINAR UNA CATEGORIA
        mis_categorias = mostrar_categorias(mi_ruta)
        la_categoria = elegir_categoria(mis_categorias)
        ruta_completa_categoria = Path(mi_ruta, la_categoria)
        eliminar_categoria(ruta_completa_categoria)
        volver_inicio()
    elif menu == 6:
        finalizar_programa =  True