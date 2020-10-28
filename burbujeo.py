# -*- coding: utf-8 -*-

# butbujeo.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 11.2: Burbujeo


def ord_burbujeo(lista):
    
    def burbujear(lista):
        global comps
        i = 0
        while i < len(lista) - 1:
            # print(i)
            comps += 1
            if lista[i] < lista[i+1]:
                pass
            else:
                # Switch
                lista[i], lista[i+1] = lista[i+1], lista[i]
            i += 1

    for i in range(1, len(lista) + 1):
        # print('DEBUG:', lista)
        burbujear(lista)

    return lista

# T ~ N^2, recorro la lista N veces haciendo N comparaciones