#manejo de los argumentos kwargs indefinidos en funciones 
#Ejemplo: persona(nombre="Juan", edad=20, ciudad="Lima")

def AnalizarArgs(**kwargs):

    numeros=[]  
    strings=[]
    otros=[]

    for clave,valor in kwargs.items():
        if isinstance(valor,int) or isinstance(valor,float):
            numeros.append((clave,valor))
        elif isinstance(valor,str):
            strings.append((clave,valor))
        else:
            otros.append((clave,valor))

    return {
        "cantidad":len(kwargs),
        "numeros":numeros,
        "strings":strings,
        "otros":otros
    }

print(AnalizarArgs(nombre="Juan", edad=20, ciudad="Lima", altura=1.75, hobbies=["leer","correr"], casado=False))
