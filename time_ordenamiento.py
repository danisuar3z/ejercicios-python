# -*- coding: utf-8 -*-

# time_ordenamiento.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 11.8: Comparaciones usando timeit.timeit

import random
from timeit import timeit
import matplotlib.pyplot as plt

# =============================================================================
# Seleccion
# =============================================================================

def ord_seleccion(lista):
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

# =============================================================================
# Insercion
# =============================================================================

def ord_insercion(lista):
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

# =============================================================================
# Burbujeo
# =============================================================================

def ord_burbujeo(lista):
    def burbujear(lista):
        i = 0
        while i < len(lista) - 1:
            if lista[i] < lista[i+1]:
                pass
            else:
                # Switch
                lista[i], lista[i+1] = lista[i+1], lista[i]
            i += 1

    for i in range(1, len(lista) + 1):
        burbujear(lista)

    return lista

# =============================================================================
# Merge Sort
# =============================================================================

def merge_sort(lista):
    if len(lista) <= 1:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

# %%

def generar_lista(N):
    return [random.randint(1, 1000) for _ in range(N)]

def crear_listas(N=256):
    listas = []
    for i in range(1, N + 1):
        listas.append(generar_lista(i))
    return listas

def exp_timeit(listas, num=1):
    methods = ['ord_seleccion', 'ord_insercion',
               'ord_burbujeo', 'merge_sort']
    tiempos = {'sel': [], 'ins': [], 'bur': [], 'e_s': []}
    i = 0
    for method in methods:
        print(method)
        global lista
        for lista in listas:
            if not i%100:
                print(i)
            i+=1
            tiempos[method[4:7]].append(timeit(method + '(lista.copy())', number=num, globals=globals()))
    return tiempos

def graficar(tiempos):
    x = list(range(len(tiempos['ins'])))
    plt.plot(x, tiempos['sel'])
    plt.plot(x, tiempos['ins'])
    plt.plot(x, tiempos['bur'])
    plt.plot(x, tiempos['e_s'])
    plt.legend(['Seleccion', 'Insercion', 'Burbujeo', 'Merge-Sort'])
    plt.title('Comparacion entre algoritmos de comparacion')
    plt.xlabel('Longitud de lista')
    plt.ylabel('Tiempo')


if __name__ == '__main__':
    tiempos = exp_timeit(crear_listas(), 10)
    graficar(tiempos)
