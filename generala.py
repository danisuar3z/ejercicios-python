# generala.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 4.7: Generala no necesariamente servida

import random
from collections import Counter
from time import time # Para registrar el tiempo de ejecución

def tirar():
    '''
    Simula una tirada de 5 dados y 
    devuelve una lista con los valores
    obtenidos.
    '''
    tirada = [random.randint(1,6) for i in range(5)]
    return tirada


def es_generala(tirada):
    '''
    Recibe una tirada y devuelve True si
    es generala, sino False.
    '''
    generala = False
    if max(tirada) == min(tirada):
        generala = True
    return generala


def tirar_de_nuevo(tirada):
    '''
    Recibe una tirada y se queda con 
    los dados más repetidos para luego
    volver a tirar los descartados y 
    devolver la nueva tirada.
    '''
    contador_dados = Counter()
    # Cuento las repeticiones de cada dado en la tirada
    for dado in tirada:
        contador_dados[dado] += 1
    # Me quedo solo con los que más se repiten, si hay empate o 
    # ninguno se repite me quedo con el primero
    tirada = [dado for dado in tirada 
              if dado == contador_dados.most_common(1)[0][0]]
    # Vuelvo a tirar los dados descartados
    tirada += [random.randint(1,6) for i in range(5-len(tirada))]
    return tirada


def mano():
    '''
    Devuelve la tirada final luego de intentar 
    sacar generala dentro de los 3 tiros.
    '''
    tirada = tirar()
    i = 1
    # Mientras la tirada no sea generala
    while not es_generala(tirada):
        if i == 3: # Corto luego de la segunda re-tirada
            break
        tirada = tirar_de_nuevo(tirada)
        i += 1
    return tirada


#%%

# Estimo la probabilidad de sacar generala en las (hasta) 3
# tiradas de una mano

ti = time() # Tiempo inicial
N = 100000

salio_generala = [es_generala(mano()) for i in range(N)]
G = sum(salio_generala)
prob = G/N
probreal = 1
tiempo = time() - ti # Tiempo transcurrido

#%%

# Printeo resultados

print(f'En {N:,} manos se lograron {G} generalas.\n'
      f'Probabilidad aproximada:       {100*prob:.4f}%\n'
      f'Probabiliad generala servida:  {100*(1/6)**4:.4f}%\n')
print(f'El tiempo de ejecución fue de {tiempo:.2f} segundos.')

'''
En 100,000 manos se lograron 4551 generalas.
Probabilidad aproximada:       4.5510%
Probabiliad generala servida:  0.0772%

El tiempo de ejecución fue de 3.96 segundos.
'''
