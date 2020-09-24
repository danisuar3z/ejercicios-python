# busqueda_en_listas.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicios de busqueda en listas

# Ejercicio 3.6: Busquedas de un elemento

def buscar_ult_elemento(lista, e):
    """
    Si e esta en la lista devuelve su ultimo indice, 
    sino devuelve -1.
    """
    indices = []
    for i, elemento in enumerate(lista):
        if elemento == e:
            indices.append(i) # Guardo todos los indices de aparicion
    if indices == []:
        return -1
    else:
        return indices[-1] # Le pido el ultimo valor

# buscar_ult_elemento([1,2,3,2,3,4],1) # Salida:  0
# buscar_ult_elemento([1,2,3,2,3,4],2) # Salida:  3
# buscar_ult_elemento([1,2,3,2,3,4],3) # Salida:  4
# buscar_ult_elemento([1,2,3,2,3,4],5) # Salida: -1

#%%

def buscar_n_elemento(lista, e):
    """
    Si e esta en la lista devuelve la cantidad de veces, 
    sino devuelve -1.
    """
    indices = []
    for i, elemento in enumerate(lista):
        if elemento == e:
            indices.append(i)
    if indices == []:
        return -1
    return len(indices)

# buscar_n_elemento([1,2,3,2,1], 1) # Salida:  2
# buscar_n_elemento([1,2,3,2,1], 3) # Salida:  1
# buscar_n_elemento([1,2,3,2,1], 0) # Salida: -1
#%%
# Ejercicio 3.7: Búsqueda de máximo y mínimo

def maximo(lista):
    """
    Devuelve el maximo valor de una lista de numeros.
    """
    for i, e in enumerate(lista):
        if i == 0: # Para no empezar con m = 0
            m = e  # y que funcione para numeros negativos
            continue # Fuerzo a volver al for
        if e > m:
            m = e
    return m

# maximo([1,2,7,2,3,4]) # Salida:  7
# maximo([1,2,3,4])     # Salida:  4
# maximo([-5,4])        # Salida:  4
# maximo([-5,-4])       # Salida: -5
#%%
def minimo(lista):
    """
    Devuelve el minimo valor de una lista de numeros.
    """
    for i, e in enumerate(lista):
        if i == 0:
            m = e
            continue
        if e < m: # Es igual a la anterior salvo este paso
            m = e
    return m

# minimo([0,-1,2,1.5,3.5]) # Salida: -1
