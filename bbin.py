# -*- coding: utf-8 -*-

# bbin.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.4: Búsqueda binaria


def donde_insertar(lista, e, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si e está en lista
    Si e no estaba devuelve la posicion en la que se 
    podria insertar y siga quedando ordenada la lista.
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == e:
            pos = medio     # elemento encontrado!
        if lista[medio] > e:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < e:
            izq = medio + 1 # descarto mitad izquierda
    # Hasta aca el codigo es el mismo, y si no se encontro
    # el valor pedido, le asigno la posicion izq
    if pos == -1:
        pos = izq
    return pos


def insertar(lista, e):
    '''
    Inserta un valor en una lista ordenada si no está 
    presente y devuelve su posición y la lista. De lo 
    contrario solo devuelve su posición.
    '''
    pos = donde_insertar(lista, e)
    if lista[pos] != e:
        lista.insert(pos, e)
        return pos, lista
    return pos

