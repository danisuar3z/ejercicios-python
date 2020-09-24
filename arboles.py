# -*- coding: utf8 -*-

# arboles.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# 3.6 Arbolado porteño y comprensión de listas

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

'''
Este archivo fue modificado múltiples veces a esta altura. 
Dejo algunas cosas comentadas para no borrarlas así no las 
pierdo.
'''


# Ejercicio 3.18: Lectura de todos los árboles

def leer_arboles(nombre_archivo):
    '''
    Recibe un .csv con datos de árboles y 
    devuelve una lista de diccionarios con 
    la información de cada uno.
    '''
    arboleda = []
    f = open(nombre_archivo, 'rt', encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    # Genero una lista con los tipos de objeto que quiero obtener para
    # cada columna
    types = [float, float, int, int, int, int, int, str, str, str, str, str,
             str, str, str, float, float]
    # Uso comprension de listas para crear arboleda y convertir sus valores
    arboleda = [{nombre: func(val) for nombre, func, val in 
                 zip(headers, types, row)} for row in rows]
    f.close()
    print(f'La cantidad de arboles es {len(arboleda)}.') # Para checkear
    return arboleda

#%%
# Ejercicio 3.19: Lista de altos de Jacarandá

archivo = 'Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(archivo)
alt_jac = [arbol['altura_tot'] for arbol in arboleda if
           arbol['nombre_com'] == 'Jacarandá']
# len(alt_jac) # Salida: 3255
#%%

# Ejercicio 4.30: Histograma de altos de Jacarandás

plt.hist(alt_jac, bins=25)


#%%

# Ejercicio 3.20: Lista de altos y diámetros de Jacarandá

altdiam = [(arbol['altura_tot'], arbol['diametro']) for arbol in
                  arboleda if arbol['nombre_com'] == 'Jacarandá']
# altdiam[:4]    # Salida: [(5, 10), (5, 10), (5, 10), (5, 10)]

#%%

# Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás

# Primero unpackeo las tuplas
x, y = zip(*altdiam)

# Ploteo
plt.scatter(x, y)

#%%

# Usando NumPy

altdiam_array = np.array(altdiam, dtype='int,int')
x, y = altdiam_array['f0'], altdiam_array['f1']
colors = np.random.rand(len(altdiam))

#%%

# Ploteo
plt.scatter(x, y, s=40, c=colors, alpha=0.2)
plt.xlabel('diametro (cm)')
plt.ylabel('alto (m)')
plt.title('Relación diámetro-alto de Jacarandás')

#%%

# Ejercicio 3.21: Diccionario con medidas
def medidas_de_especies(especies, arboleda):
    '''
    Recibe una lista de nombres de especies 
    y una lista con información de árboles y 
    devuelve un diccio. con pares de tuplas 
    para cada especie con la altura y diám. 
    de cada espécimen.
    '''
    alt_diam = {especie: [(arbol['altura_tot'], arbol['diametro']) 
                          for arbol in arboleda 
                          if arbol['nombre_com'] == especie] 
                          for especie in especies}
    return alt_diam

#%%

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

#%%

# Desempaqueto los valores

medidas_euca = np.array(medidas[especies[0]], dtype='int,int')
xe, ye = medidas_euca['f0'], medidas_euca['f1']

medidas_palo = np.array(medidas[especies[1]], dtype='int,int')
xp, yp = medidas_palo['f0'], medidas_palo['f1']

medidas_jac = np.array(medidas[especies[2]], dtype='int,int')
xj, yj = medidas_jac['f0'], medidas_jac['f1']

#%%
# PYPLOT

# Creo grilla de 1x3 plots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True)
fig.suptitle('Relaciones altura-diámetro')

# Genero colores al azar para cada set de datos
colors1 = np.random.rand(len(medidas[especies[0]]))
colors2 = np.random.rand(len(medidas[especies[1]]))
colors3 = np.random.rand(len(medidas[especies[2]]))

# Nombre de los ejes
for ax in (ax1, ax2, ax3):
    ax.set(xlabel='diametro (cm)', ylabel='altura (m)')

# Seteo límites de los ejes (con sharex/y los compartimos)
plt.xlim(-1,40)
plt.ylim(-1,200)

# Títulos de los subplots
ax1.set_title(f'{especies[0]}')
ax2.set_title(f'{especies[1]}')
ax3.set_title(f'{especies[2]}')

# Ploteo
ax1.scatter(xe, ye, s=30, c=colors1, alpha=0.2)
ax2.scatter(xp, yp, s=30, c=colors2, alpha=0.2)
ax3.scatter(xj, yj, s=30, c=colors3, alpha=0.2)

#plt.show()

#%%

# Extra: ¿podés hacer un solo gráfico que muestre 
# dos de estas tres especies en diferentes colores 
# y resulte claro? ¿Y las tres especies?

plt.title('Relación altura-diámetro de 3 especies')
plt.xlabel('diámetro (cm)')
plt.ylabel('altura (m)')
plt.xlim(-0.5, 50)
plt.ylim(-5, 250)

# Ploteo
plt.scatter(xe, ye, s=50, c='blue', alpha=0.2, label=especies[0])
plt.scatter(xp, yp, s=50, c='darkgreen', alpha=0.2, label=especies[1])
plt.scatter(xj, yj, s=50, c='orange', alpha=0.2, label=especies[2])

# Cuadrícula
plt.grid(True)

# Creo leyenda
legend = plt.legend(loc='best', shadow=True, fontsize='large', framealpha=0.5)
legend.get_frame().set_facecolor('C7')

# Opacidad de la leyenda
for lh in legend.legendHandles: 
    lh.set_alpha(1)

#plt.show()

#%%

# CODIGO DE LAS CLASES ANTERIORES

# Compruebo
print(f' {"Especie":^21s}  {"Cant":^4s}')
print(f' {"-"*27}')
for especie in especies:
    print(f' {especie:<21s}: {len(medidas[especie]):>4d}', end='')
    print('')

#%%
# CODIGO ENTREGADO PARA LA CLASE 2
# Ej 2.22: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
    """
    Devuelve lista de diccionarios con todos los arboles de un parque
    y su info e imprime la cantidad total.
    """
    arboles_parque = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        headers = next(f).split(',')
        headers[-1] = headers[-1].replace('\n','') # elimino el enter
        
        rows = csv.reader(f)        
        for row in rows: # Solo convierto los parametros usados
            arbol = dict(zip(headers, row))
            if (arbol['espacio_ve'].upper() == parque.upper()):
                arbol['altura_tot'] = int(arbol['altura_tot'])
                arbol['inclinacio'] = int(arbol['inclinacio'])
                arboles_parque.append(arbol)
            else: # No se si es conveniente usar esto o dejar vacio
                pass
    print(f'Cantidad de arboles en parque {parque}: {len(arboles_parque)}.')
    return arboles_parque

# Ej 2.23: Determinar las especies en un parque
def especies(lista_arboles):
    """
    Toma una lista de arboles y devuelve un conjunto con las especies.
    """
    arboles = []
    for arbol in lista_arboles:
        # Saco las especies no determinables
        if (arbol['nombre_com'].lower() == 'no determinable' or 
        arbol['nombre_com'].lower() == 'no determinado'):
                pass # asi no agrego estos casos al conjunto
        else:
            arboles.append(arbol['nombre_com'])
    conjunto_arboles = set(arboles) # podria haber trabajado con un set
    return conjunto_arboles         # desde el principio

# Ej 2.24: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
    """
    Recibe una lista de diccionarios de arboles y devuelve otro
    diccionario con los nombres como claves y cantidad de arboles
    como valores.
    """
    contador_especies = Counter()
    for arbol in lista_arboles:
        contador_especies[arbol['nombre_com']] += 1 # sumo uno por cada
    return contador_especies                      # aparicion del arbol


# calculo los 5 mas comunes de los 3 parques pedidos
archivo = 'Data/arbolado-en-espacios-verdes.csv'
tres_parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

# Obtengo las listas con leer_parque y las guardo en otra lista
arboles_tres_parques = []
for parque in tres_parques:
    arboles_tres_parques.append(leer_parque(archivo, parque))

lista_most_common = []
for parque in arboles_tres_parques:
    lista_most_common.append(contar_ejemplares(parque).most_common(5))

# Imprimo tablita linda
print(f'{"-" * 81}\n{"LAS 5 ESPECIES DE ARBOLES MAS COMUNES":^81}')
print("-"*81)
print(f'{tres_parques[0]:^26}|{tres_parques[1]:^26}|{tres_parques[2]:^26}')
print(f'{"-"*81}\n{"Especie":^21}|{"Cant":^4}|'
      f'{"Especie":^21}|{"Cant":^4}|{"Especie":^21}|{"Cant":^4}|')
print("-"*81)
for i in range(len(lista_most_common[0])):
    for j in range(3):
        print(f'{lista_most_common[j][i][0]:21}|'
              f'{lista_most_common[j][i][1]:>4}|', end='')
    print('')
print('\n')

# Ej 2.25: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
    """
    Recibe una lista de arboles y el nombre de una especie y devuelve
    una lista con todas las alturas de esa especie.
    """
    lista_alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].upper() == especie.upper():
            lista_alturas.append(arbol['altura_tot'])
    lista_alturas.sort() # no es necesario pero ordeno los valores
    return lista_alturas # para que quede mas linda la lista

# Defino funcion promedio para mayor comodidad
def mean(a):
    return sum(a)/len(a)

# Altura maxima y promedio de Jacarandá en los tres parques

# Obtengo las alturas y las guardo en una lista
alturas_parques = []
for parque in arboles_tres_parques:
    alturas_parques.append(obtener_alturas(parque, 'Jacarandá'))

# Calculo los maximos y promedios y los guardo en otra lista
max_parques = []
mean_parques = []
for parque in alturas_parques:
    max_parques.append(max(parque))
    mean_parques.append(mean(parque))

# Imprimo tablita
print(f'{"-" * 51}\n{"Altura de Jacarandás":^51}\n{"-" * 51}\n'
      f'{"Medida":^9} | {"General Paz":^11} | {"Los Andes":^11} | '
      f'{"Centenario":^11}\n{"-" * 51}')
print(f'{" max  / m":<9}', end='')
for i in range(len(max_parques)):
    print(f' | {max_parques[i]:>11}', end='')
print(f'\n{" prom./ m":<9}', end='')
for i in range(len(mean_parques)):
    print(f' | {mean_parques[i]:>11.2f}', end='')
print('\n')

# Ej 2.26: Inclinacion promedio por especie de una lista
def obtener_inclinaciones(lista_arboles, especie):
    """
    Recibe una lista de arboles y una especie y devuelve una lista
    con todas las inclinaciones de esa especie.
    """
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].upper() == especie.upper():
            lista_inclinaciones.append(arbol['inclinacio'])
    lista_inclinaciones.sort()
    return lista_inclinaciones


# Ej 2.27: Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
    """
    Toma una lista de arboles y devuelve el especimen mas inclinado.
    """
    contador_inclinacion = Counter()
    for especie in especies(lista_arboles):
        contador_inclinacion[especie] = max(obtener_inclinaciones(
                                                lista_arboles, especie))
    return contador_inclinacion.most_common(1)

print(f'La especie mas inclinada en el parque {tres_parques[2]} es\n'
      f'{especimen_mas_inclinado(arboles_tres_parques[2])}')
# Salida: La especie mas inclinada en el parque CENTENARIO es 
#         [('Falso Guayabo (Guayaba del Brasil)', 80)]


# Ej 2.28: Especie con más inclinada en promedio
def especie_promedio_mas_inclinada(lista_arboles):
    """
    Toma una lista de arboles de un parque y devuelve la especie mas
    inclinada en promedio
    """
    contador_inclinacion = Counter()
    for especie in especies(lista_arboles):
        contador_inclinacion[especie] = round(mean(
            obtener_inclinaciones(lista_arboles, especie)), 1)
    return contador_inclinacion.most_common(1)

print(f'La especie mas inclinada en promedio en el parque\n{tres_parques[1]}'
      f' es {especie_promedio_mas_inclinada(arboles_tres_parques[1])}')
# Salida: La especie mas inclinada en promedio en el parque
#         ANDES, LOS es [('Álamo plateado', 25.0)]


"""
Para tener resultados de toda la ciudad se podria definir una funcion
leer_ciudad() que devuelva un diccionario con la informacion de todos
los arboles en el archivo descargado de la pagina del gobierno de CABA,
y luego trabajar con las mismas funciones que definimos.
"""
#%%
#PRUEBA

archivo = 'Data/arbolado-en-espacios-verdes.csv'
centenario = leer_parque(archivo, 'CENTENARIO')
gral_paz = leer_parque(archivo, 'GENERAL PAZ')
andes = leer_parque(archivo, 'ANDES, LOS')
parques = {'Parque Centenario': centenario, 'Parque General Paz': gral_paz, 'Parque Los Andes': andes}
#%%
## Resultados ##
for parque, variable in parques.items(): 
    
    alturas_jacarandas = obtener_alturas(variable, 'Jacarandá')
    jacaranda_max_alto = round(max(alturas_jacarandas), 3)
    # En otros parques donde no haya jacarandás se tiene que modificar la siguiente linea
    jacaranda_altura_promedio = round(sum(alturas_jacarandas) / len(alturas_jacarandas), 3)
    inclinacion_promedio_max = especie_promedio_mas_inclinada(variable)
    inclinacion_max = especimen_mas_inclinado(variable)
    especies_mas_comunes = contar_ejemplares(variable).most_common(5)
    print(f' {parque}')
    print(' ' + '~' * len(parque))
    print(' 5 especímenes mas comunes')
    header = ['Espécimen', 'Cantidad']
    print(' ' + '~' * 44)
    print(f' | {header[0]:>20s}{header[1]:>20s} |')
    print(' ' + '~' * 44)
    for j, i in especies_mas_comunes:
        print(f' | {j:>20s}{i:>20d} |')
    print(' ' + '~' * 44)
    print(f' Jacarandá mas alto: {jacaranda_max_alto} mts. Altura media del Jacarandá: {jacaranda_altura_promedio} mts')
    print(f' Ejemplar con mayor inclinación: {inclinacion_max[0][1]} con {inclinacion_max[0][0]} grados')
    print(f' Ejemplar con mayor inclinación media: {inclinacion_promedio_max[0][1]} con {inclinacion_promedio_max[0][0]} grados')
    print('')
    print('')
