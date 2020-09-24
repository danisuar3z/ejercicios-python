# -*- coding: utf-8 -*-

# .py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.17: 

import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_binaria(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comparaciones = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones += 1 # Primera comparacion
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break # Me ahorro algunas comparaciones si lo encuentro
        comparaciones += 1 # Segunda comparacion
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        pos = izq
    return pos, comparaciones


def busqueda_secuencial_(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 #sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps


def generar_lista(longitud, lim_sup):
    '''
    Devuelve una lista ordenada del largo ingresado, 
    con una muestra al azar entre 0 y el lim_sup.
    '''
    lista = random.sample(range(lim_sup), k=longitud)
    lista.sort()
    return lista


def generar_elemento(lim_sup):
    '''
    Devuelve un entero entre 0 y el lim_sup.
    '''
    elem = random.randint(0, lim_sup-1)
    return elem


def experimento_secuencial_promedio(lista,lim_sup,repeticiones):
    '''
    Repite la busqueda secuencial para la cantidad de 
    repeticiones ingresada con valores al azar cada vez.
    Cuenta las comparaciones y las promedia y devuelve 
    este valor.
    '''
    comps_tot = 0
    for i in range(repeticiones):
        e = generar_elemento(lim_sup)
        comps_tot += busqueda_secuencial_(lista,e)[1]

    comps_prom = comps_tot / repeticiones
    return comps_prom


def experimento_binario_promedio(lista, lim_sup, repeticiones):
    '''
    Repite la busqueda binaria para la cantidad de
    repeticiones ingresada con valores al azar cada vez.
    Cuenta las comparaciones, las promedia y devuelve el
    valor.
    '''
    comps_tot = 0
    for i in range(repeticiones):
        e = generar_elemento(lim_sup)
        comps_tot += busqueda_binaria(lista, e)[1]
    
    comps_prom = comps_tot / repeticiones
    return comps_prom


#%%
# Realizo los experimentos

lim_sup = 10000
repeticiones = 1000

largos = np.arange(256)+1 # estos son los largos de listas que voy a usar
comps_promedio_sec = np.zeros(256) # guardo los promedios de comparaciones
comps_promedio_bin = np.zeros(256) # para cada búsqueda

for i, n in enumerate(largos):
    lista = generar_lista(n, lim_sup) # genero lista de largo n
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista,lim_sup,repeticiones)
    comps_promedio_bin[i] = experimento_binario_promedio(lista,lim_sup,repeticiones)

#%%

# grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio_sec,label='Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.plot(largos,comps_promedio_bin,label='Búsqueda Binaria')
plt.title("Complejidad de la Búsqueda")
#plt.ylim(0,30) # Para ver la relacion mas comodamente
plt.legend()

























