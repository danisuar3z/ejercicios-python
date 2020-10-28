# -*- coding: utf-8 -*-

# comparaciones_ordenamiento.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 11.5: comparar métodos gráficamente

import random

import matplotlib.pyplot as plt
# %%
# Metodos

# =============================================================================
# Seleccion
# =============================================================================

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    global comps
    comps += b - a
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

# =============================================================================
# Insercion
# =============================================================================

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    global comps
    for i in range(len(lista) - 1):
        comps += 1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        # print("DEBUG: ", lista)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    global comps
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        comps += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

# =============================================================================
# Burbujeo
# =============================================================================

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
    global comps
    while(i < len(lista1) and j < len(lista2)):
        comps += 1
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

def comparar(largo_max=256, N_max=1000):
    global comps
    comps_sel, comps_ins, comps_msort, comps_bur = [], [], [], []
    for i in range(1, largo_max + 1):
        lista = generar_lista(i)
        comps = 0
        
        copia = lista.copy()
        ord_seleccion(copia)
        comps_sel.append(comps)
        
        comps = 0
        copia = lista.copy()
        ord_insercion(copia)
        comps_ins.append(comps)

        comps = 0
        copia = lista.copy()
        merge_sort(copia)
        comps_msort.append(comps)

        comps = 0
        ord_burbujeo(lista)
        comps_bur.append(comps)
    return comps_sel, comps_ins, comps_msort, comps_bur

def graficar(l_sel, l_ins, l_msort, l_bur):
    x = list(range(len(l_sel)))
    plt.plot(x, l_sel)
    plt.plot(x, l_ins)
    plt.plot(x, l_msort)
    plt.plot(x, l_bur)
    plt.legend(['Seleccion', 'Insercion', 'Merge-Sort', 'Burbujeo'])
    plt.title('Comparacion entre algoritmos de comparacion')
    plt.xlabel('Longitud de lista')
    plt.ylabel('Cantidad de comparaciones realizadas')
    
# %%

if __name__ == '__main__':
    sel, ins, msort, bur = comparar()
    graficar(sel, ins, msort, bur)
