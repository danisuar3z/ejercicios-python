# -*- coding: utf-8 -*-

# envido.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 4.8: Envido

import random
from collections import Counter
from time import time # Para chusmear cuánto tarda en correr el script

#%%

# GENERO EL MAZO DE CARTAS ESPAÑOLAS (sin 8s ni 9s)

def crear_mazo():
    '''
    Genera el mazo de cartas españolas 
    sin 8 ni 9. Devuelve una lista de 
    tuplas con los valores y palos.
    '''
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    cartas = [(valor, palo) for valor in valores for palo in palos]
    return cartas


def mano_truco():
    '''
    Requiere que esté definido el mazo de cartas
    y devuelve una lista de 3 cartas (tuplas) 
    obtenidas sin reposición.
    '''
    mano = random.sample(crear_mazo(), k=3)
    return mano


def cuanto_vale(valor):
    '''
    Recibe un valor de carta y devuelve el
    número que aporta al envido.
    '''
    if valor in range(1,8):
        vale = valor + 10
    else:
        vale = 10
    return vale
    

def envido(mano):
    '''
    Recibe una mano de cartas y devuelve el 
    valor del envido.
    '''
    envido = 0
    contador_palos = Counter()
    for valor, palo in mano:
        contador_palos[palo] += 1
    
    # Ningún palo repetido
    if len(contador_palos) == 3:
        # Las figuras (10, 11 y 12) no aportan al envido en estos casos
        # Y los valores comunes solo aportan su valor exacto
        valores = [cuanto_vale(valor)-10 for valor, palo in mano]
        envido += max(valores) # Toma el valor máximo
    
    # Flor! (los 3 palos iguales)
    elif len(contador_palos) == 1:
        valores = [cuanto_vale(valor) for valor, palo in mano]
        # Me quedo con las dos cartas que generen mayor envido
        envido += sum(valores) - min(valores)
    
    # 2 cartas iguales
    else:
        # Guardo en una variable el palo a calcularle envido
        palo_envido = contador_palos.most_common(1)[0][0]
        for valor, palo in mano:
            if palo == palo_envido:
                envido += cuanto_vale(valor)
    return envido

#%%

# Genero muchas manos para estimar las probabilidades 
# de obtener 31, 32 Y 33 de envido

ti = time() # Inicio el contador de tiempo
N = 100000

saque_31, saque_32, saque_33 = [], [], []

for i in range(N):
    mano = mano_truco()
    if envido(mano) == 31:
        saque_31.append(True)
    elif envido(mano) == 32:
        saque_32.append(True)
    elif envido(mano) == 33:
        saque_33.append(True)

N_31, N_32, N_33 = sum(saque_31), sum(saque_32), sum(saque_33)
prob_31, prob_32, prob_33 = N_31/N, N_32/N, N_33/N

tiempo = time() - ti # Finalizo el contador de tiempo

#%%

# PRINTEO RESULTADOS

print(f' Se simularon {N:,} manos de truco y se obtuvieron los siguientes'
      f' resultados:\n'
      f' {"-"*24}\n'
      f' {"Envido":^6} | {"N":^5} | {"Prob.":^5}\n'
      f' {"-"*24}\n'
      f' {"31":>6} | {N_31:^5} | {prob_31*100:^5.2f}%\n'
      f' {"32":>6} | {N_32:^5} | {prob_32*100:^5.2f}%\n'
      f' {"33":>6} | {N_33:^5} | {prob_33*100:^5.2f}%\n'
      f' {"-"*24}\n'
      f' El tiempo de ejecución del script fue de {tiempo:.2f} segundos.'
      )
	
#%%

'''
SALIDA:
 Se simularon 100,000 manos de truco y se obtuvieron los siguientes
 resultados:
 ------------------------
 Envido |  N   | Prob.
 ------------------------
     31 | 3035 | 3.03 %
     32 | 1433 | 1.43 %
     33 | 1473 | 1.47 %
 ------------------------
 El tiempo de ejecución del script fue de 2.10 segundos.
 '''
 
# Tiene sentido que la probabilidad de obtener 32 y 33 de envido sea 
# similar ya que hay solo una combinación posible por palo para obtener
# ese valor (6+7), mientras que para obtener 31 hay dos combinaciones
# posibles por palo (5+6 y 4+7)
 
 #%%
 
# Bonus track: probabilidad de sacar flor
 
def es_flor(mano):
    '''
    '''
    flor = False
    if (mano[0][1] == mano[1][1] and 
        mano[0][1] == mano[2][1]):
        flor = True
    return flor

N = 100000
ti = time()
saque_flor = [es_flor(mano_truco()) for i in range(N)]

prob_flor = sum(saque_flor)/N
tf = time()
print(f'\n BONUS TRACK: Flor edition\n'
      f' Se simularon {N:,} manos y se obtuvo flor {sum(saque_flor)} veces.\n'
      f' La probabilidad aproximada es de {prob_flor*100:.2f}%.\n'
      f' El tiempo de ejecución fue de {tf-ti:.2f} segundos.')

'''
SALIDA:
BONUS TRACK: Flor edition
Se simularon 1,000,000 manos y se obtuvo flor 48341 veces.
La probabilidad aproximada es de 4.83%.
El tiempo de ejecución fue de 9.85 segundos.
'''
