

def obtener_numero_inter(tupla):
       if not isinstance(tupla, tuple):
        raise TypeError("El argumento debe ser una tupla")
       
       if len(tupla) != 3:
            raise ValueError("La tupla debe tener exactamente 3 elementos")

       if len(set(tupla)) < 3:
            raise ValueError("Los valores deben ser distintos")

       ordenados = sorted(tupla)
       return ordenados[1]

def devolver_distintos(*args):
    print(len(args))
    if len(args) != 3:
        raise ValueError("Se deben proporcionar al menos tres argumentos.")

    for i in args:
        if not isinstance(i, (int, float)):
            raise ValueError("Todos los argumentos deben ser números.")
        
    suma = 0
    
    for numero in args:
        suma += numero

    print(suma)
    if suma > 15:
        return max(args)

    if suma < 10:
        return min(args)
    else: 
        return obtener_numero_inter(args)
    
print(devolver_distintos(3,6,9,4))  # Debería devolver 3
#print(devolver_distintos(1,2,3))        # Debería devolver 2
    
