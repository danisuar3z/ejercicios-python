# -*- coding: utf-8 -*-

# propaga.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 3.9: Propagacion

# Pruebo versión lineal

def propagar(lista):
    
    for i, f in enumerate(lista):
        if i != len(lista)-1 and f == 1 and lista[i+1] == 0:
            lista[i+1] = 1
    for i, f in enumerate(lista[::-1]): # No funciona porque es otra lista
        if i != len(lista)-1 and f == 1 and lista[::-1][i+1] == 0:
            lista[-i-2] = 1
    return lista

print(propagar([0,0,1]))
#%%
# VERSION ENTREGADA
# Copio la funcion del ejercicio anterior ya que la uso en propagar()
def busqueda_lineal(lista, e):
    """
    Si e esta en la lista te devuelvela cantidad de apariciones,
    sino te devuelve -1
    """
    indices = []
    for i, elemento in enumerate(lista):
        if elemento == e:
            indices.append(i)
    if indices == []:
        return -1
    else:
        return len(indices)

#%%

def propagar(lista_recibida):
    """
    Propaga los 1 a los 0, interrumpiendo la propagacion por los -1.
    Devuelve una nueva lista.
    """
    # Trabajo con una copia para no perder la original
    lista = lista_recibida.copy()
    # Cubro primero los casos "faciles" para disminuir
    # iteraciones innecesarias en esos casos
    if -1 not in lista:
        # Si hay algun 1 convierto todo a unos
        if 1 in lista:
            for i in range(len(lista)):
                lista[i] = 1
        # Si no hay ningun 1 devuelvo la lista tal cual
    # Ahora con -1 presentes
    else:
        # Si no hay ningun 1 devuelvo la lista tal cual
        if 1 not in lista:
            pass
        # Aca empieza lo heavy. Hay -1, 0 y 1
        else:
            # Optimizo las iteraciones del while con una idea del
            # compañero Lucas Ezquerra (es mejor que < len(lista))
            repito = busqueda_lineal(lista_recibida, 0)
            contador = 0
            while contador < repito:
                # Recorro los fosforos de izq a der
                for i, f in enumerate(lista):
                    # Si me encuentro con un -1 paso al proximo fosforo
                    if f == -1:
                        #contador += 1
                        continue
                    # Salvedades para primera y ultima posicion
                    elif i == 0:
                        if f == 1:
                            if lista[i+1] != -1:
                                lista[i+1] = 1
                    elif i == len(lista)-1:
                        if f == 1:
                            if lista[i-1] != -1:
                                lista[i-1] = 1
                    # Si no era ninguno de esos casos, sigo
                    elif f == 1:
                        if lista[i-1] != -1:
                            lista[i-1] = 1
                        if lista[i+1] != -1:
                            lista[i+1] = 1
                contador += 1
    return lista

#%%

lista = [0,-1,0,0,0,1]
print(f'La cantidad de ceros en la lista es {busqueda_lineal(lista, 0)}.'
      f'\n{lista} => {propagar(lista)}')
# Salida: La cantidad de ceros en la lista es 4
#         [0, -1, 0, 0, 0, 1] => [0, -1, 1, 1, 1, 1]
