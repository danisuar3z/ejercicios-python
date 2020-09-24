# -*- coding: utf-8 -*-

# figuritas.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# 4.4: El álbum de figuritas

import random
import numpy as np
import matplotlib.pyplot as plt
from time import time


# Supongo que se compran de a una


def crear_album(total_figus):
    '''
    Devuelve un np.array con la
    cantidad de ceros recibida.
    '''
    album = np.zeros(total_figus)
    return album


def album_incompleto(album):
    '''
    True si el album tiene espacios 
    vacíos (0), sino False.
    '''
    incompleto = True
    if 0 not in album:
        incompleto = False
    return incompleto


def comprar_figu(total_figus):
    '''
    Devuelve un entero al azar entre 
    cero y el valor ingresado -1.
    '''
    figu_comprada = random.randint(0, total_figus-1) # tmb se puede
    return figu_comprada                             # np.random.randint()
                                                     # o random.choice

def cuantas_figus(total_figus):
    '''
    Simula la compra de figuritas hasta 
    llenar un album del largo recibido 
    y devuelve la cantidad comprada.
    '''
    album = crear_album(total_figus)
    while album_incompleto(album):
        album[comprar_figu(total_figus)] += 1
    cantidad_figus = sum(album)
    return cantidad_figus

#%%

total_figus = 670
cantidad_figus = cuantas_figus(total_figus)

#%%
print(f'Para llenar un álbum de 670 figuritas, se requieren comprar '
      f'{cantidad_figus:.0f} paquetes de una figurita.')

#%%

n_repeticiones = 1000
total_figus = 6

mil_veces_6 = [cuantas_figus(total_figus) for i in range(n_repeticiones)]
promedio_mil_veces_6 = np.mean(mil_veces_6)


#%%

print(f'Se simularon {n_repeticiones:,} llenados de álbumes de {total_figus} '
      f'figuritas, obteniéndose un promedio de {promedio_mil_veces_6:.0f} '
      'figus para llenarlo.\n(comprando de a 1 figurita)')

#%%

# Ejercicio 4.20:

n_repeticiones = 100
cien_veces_670 = [cuantas_figus(670) for i in range(n_repeticiones)]
promedio_cien_veces_670 = np.mean(cien_veces_670)

#%%

print(f'Se simularon {n_repeticiones:,} llenados de álbumes de 670 figuritas,'
      f' obteniéndose un promedio de {promedio_cien_veces_670:.0f} figus'
      f' para llenarlo.\n(comprando de a 1 figurita)')

'''
SALIDA:
Se simularon 100 llenados de álbumes de 670 figuritas, 
obteniéndose un promedio de 4706 figus para llenarlo.
(comprando de a 1 figurita)
'''

#%%

def comprar_paquete(total_figus, figus_por_paquete=5):
    '''
    Devuelve 5 figus (posiciones del 
    album) al azar.
    '''
    figus_paquete = np.array([np.random.randint(total_figus) for 
                     i in range(figus_por_paquete)])
    return figus_paquete

def cuantos_paquetes(total_figus, figus_por_paquete=5):
    '''
    Simula el llenado de un álbum del 
    total recibido y devuelve el nro. 
    de paquetes comprados.
    '''
    album = crear_album(total_figus)
    cantidad_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(total_figus, figus_por_paquete)
        for figu in paquete:
            album[figu] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes

#%%

ti = time()
n_repeticiones = 100

cien_veces = [cuantos_paquetes(670) for i in range(n_repeticiones)]
promedio_cien_veces = np.mean(cien_veces)

tf = time()


#%%

print(f'Se simularon {n_repeticiones:,} llenados de álbumes de 670 figuritas'
      f' obteniéndose un promedio de {promedio_cien_veces:.0f} paquetes '
      f'comprados.\nEl tiempo de ejecución del script fue de '
      f'{tf-ti:.2f} segundos')

'''
SALIDAS:
Se simularon 100 llenados de álbumes de 670 figuritas 
obteniéndose un promedio de 979 paquetes comprados.
 El tiempo de ejecución del script fue de 2.87 segundos
---
Se simularon 1,000 llenados de álbumes de 670 figuritas 
obteniéndose un promedio de 961 paquetes comprados.
El tiempo de ejecución del script fue de 28.29 segundos
'''

#%%

# Ejercicio 4.25

def menos_de(cuantos_paquetes, max_paquetes):
    '''
    Devuelve True si la cantidad de 
    paquetes es menor o igual al 
    max ingresado, sino False.
    '''
    menosde = False
    if cuantos_paquetes <= max_paquetes:
        menosde = True
    return menosde

#%%

ti = time()
N = 100
G = [menos_de(cuantos_paquetes(670), 850) for i in range(N)]
prob = sum(G)/N
tf = time()


#%%

print(f'Se simularon {N:,} llenados de álbumes de 670 figuritas y se '
      f'estimó la probabilidad de llenarlo habiendo comprado 850 paquetes '
      f'o menos, siendo la misma del {100*prob:.1f}%.\n'
      f'El tiempo de ejecución del script fue de {tf-ti:.2f} segundos')

'''
SALIDAS:
Se simularon 100 llenados de álbumes de 670 figuritas 
y se estimó la probabilidad de llenarlo habiendo comprado 
850 paquetes o menos, siendo la misma del 31.0%.
El tiempo de ejecución del script fue de 2.79 segundos
----
Se simularon 1,000 llenados de álbumes de 670 figuritas 
y se estimó la probabilidad de llenarlo habiendo comprado 
850 paquetes o menos, siendo la misma del 32.0%.
El tiempo de ejecución del script fue de 27.67 segundos
'''

#%%

# Variante propuesta usando array

ti = time()
N = 100
G = np.array([cuantos_paquetes(670) for i in range(N)])
prob = (G <= 850).sum()/N
tf = time()

#%%

plt.hist(G, bins=20, color='purple')

# Se observa distrubución con cola a derecha

#%%

# Ejercicio 4.27

# Estimo la cantidad de paquetes a comprar para tener una probabilidad
# del 90% de completar el álbum como la posición número 90 del vector 
# G creado recién, luego de ordenarlo.

G.sort()
cuantos_paquetes_90 = G[89]

print(f'La cantidad de paquetes necesaria para tener una probabilidad '
      f'del 90% de llenar el álbum es de {cuantos_paquetes_90}.')

'''
Salida:
La cantidad de paquetes necesaria para tener una 
probabilidad del 90% de llenar el álbum es de 1128.
'''
#%%

# Ejercicio 4.28: Sin repetidas en los paquetes

def comprar_paquete_2(total_figus, figus_por_paquete=5):
    '''
    Devuelve 5 figuritas distintas 
    de un total ingresado.
    '''
    num_figus = list(range(total_figus))
    # Uso random.sample para evitar tomar el mismo valor
    figus_paquete = np.array(random.sample(num_figus, k=5))
    return figus_paquete

# Defino una nueva cuantos_paquetes() para que use la nueva función

def cuantos_paquetes_2(total_figus, figus_por_paquete=5):
    '''
    Simula el llenado de un álbum del 
    total recibido y devuelve el nro. 
    de paquetes comprados.
    Versión para comprar_paquete_2()
    '''
    album = crear_album(total_figus)
    cantidad_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete_2(total_figus, figus_por_paquete)
        for figu in paquete:
            album[figu] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes

#%%


N = 100
G = np.array([cuantos_paquetes_2(670) for i in range(N)])
promedio_sin_repes = np.mean(G)
prob = (G <= 850).sum()/N


print(f'Se simularon 100 llenados de álbumes pero esta vez considerando '
      f'que no hubo repeticiones dentro de los paquetes.\n'
      f'El promedio de paquetes a comprar fue de {promedio_sin_repes} y'
      f' la probabilidad de llenarlo habiendo comprado 850 paquetes '
      f'se estimó siendo {100*prob:.1f}%.')

# No parecieran cambiar demasiado los 
# números respecto al caso anterior.

#%%

# Ejercicio 4.29: Cooperar vs competir

def albumes_incompletos(album):
    '''
    True si los 5 álbumes no están 
    llenos (me fijo que hayan más de 
    4 figus de cada una), sino False.
    '''
    incompleto = True
    if 0 not in album:
        incompleto = False
    # Esto es medio raro pero funciona. Tuve que separar al 0
    # porque sino no servía. Me pareció más cómodo que usar
    # muchos condicionales.
    if sum((1,2,3,4 not in album)) == 0:
        incompleto = False
    return incompleto

# Defino una nueva cuantos_paquetes() para incluir a esta función

def cuantos_paquetes_coop(total_figus, figus_por_paquete=5):
    '''
    Simula el llenado de un álbum del 
    total recibido y devuelve el nro. 
    de paquetes comprados.
    Versión para albumes_incompletos()
    '''
    album = crear_album(total_figus)
    cantidad_paquetes = 0
    while albumes_incompletos(album):
        paquete = comprar_paquete(total_figus, figus_por_paquete)
        for figu in paquete:
            album[figu] += 1
        cantidad_paquetes += 1
    return cantidad_paquetes

#%%

ti = time()
N = 100
G = np.array([cuantos_paquetes_coop(670) for i in range(N)])
prom_coop = np.mean(G)
prob = (G <= 200*5).sum()/N
tf = time()

#%%

print(f'Se simularon {N:,} llenados de 5 álbumes de 670 figuritas '
      f'obteniéndose un promedio de {prom_coop:.0f} paquetes '
      f'comprados y se estimó la probabilidad de llenarlo habiendo '
      f'comprado 200 paquetes cada amigue o menos, siendo la misma del '
      f'{100*prob:.1f}%.\n'
      f'\nEl tiempo de ejecución del script fue de {tf-ti:.2f} segundos.')

'''
SALIDA:
Se simularon 1000 llenados de 5 álbumes de 670 figuritas 
obteniéndose un promedio de 948 paquetes comprados y se 
estimó la probabilidad de llenarlo habiendo comprado 200 
paquetes cada amigue o menos, siendo la misma del 68.4%.

El tiempo de ejecución del script fue de 32.88 segundos.
'''
