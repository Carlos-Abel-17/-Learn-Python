#Manejo de argumentos indefinidos en funciones


def clasificar(*args):
    numeros=[]
    strings=[]
    otros=[]

    for elem in args:
        if  isinstance(elem,int) or isinstance(elem,float):
            numeros.append(elem)
        elif isinstance(elem,str):
            strings.append(elem)
        else:
            otros.append(elem)
    
    return {
        "numeros":numeros,
        "strings":strings,
        "otros":otros
    }

print(clasificar(1,2,3,"hola",4.5,[1,2],{"clave":"valor"},(5,6),"mundo"))


