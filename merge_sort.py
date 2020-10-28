# -*- coding: utf-8 -*-

# merge_sort.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Merge Sort algorithm attempt


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





















