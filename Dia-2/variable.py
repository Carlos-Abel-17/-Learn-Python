"""nombre = input('cual es tu nombre:')"""
""""print(f'bienvenido {nombre}')"""""

"""ventas = input('Cuanto vendiste:')

if(type(ventas) != 'int'):
    print('el valor ingresado no es un numero');"""


"""print(ventas)"""
""""calculo = float(ventas * 13) / 100

print(f' haz ganado: {round(calculo,2)}')"""

def calcular_comision(value):
    """value = float(value)"""
    print(type(value))
    if(type(value) != int and type(value) != float):
        print('el valor ingresado no es un numero')
        return;
    else:
        return float(value)

    calular_procentaje = value * 13 / 100;

    round(calular_procentaje, 2)

    print(calular_procentaje)
    return;



calcular_comision(input())

