# -*- coding: utf8 -*-

# bbin_rec.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 10.11: Búsqueda binaria


def bbinaria_rec(lista, e):
    # print('lista:', lista)
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        # print('medio:', medio)
        if e < lista[medio]:
            return bbinaria_rec(lista[:medio], e)
        else:
            return bbinaria_rec(lista[medio:], e)
    return res
