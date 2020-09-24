# -*- coding: utf8 -*-

# informe.py
# Daniel T. Suarez
# Ejercicio 2.15: Balances

import csv
import sys


def leer_camion(nombre_archivo):
    """
    Input: .csv file route with the contents of the truck (camion)
    Out: List of dicts with the info of every fruit.
    """
    camion = []
    with open(nombre_archivo, 'rt') as f:
        headers = next(f).split(',')
        headers[-1] = headers[-1].replace('\n','')
        rows = csv.reader(f)
        for i, row in enumerate(rows, 1):
            try:
                fruta = dict(zip(headers, row))
                fruta['cajones'] = int(fruta['cajones'])
                fruta['precio'] = float(fruta['precio'])
                camion.append(fruta)
            except ValueError:
                print(f'Error en linea {i}: No se puede interpretar '
                  f'{row}')
    return camion

def leer_precios(nombre_archivo):
    """
    Input: List of selling prices.
    Out: Dict with names as keys and prices as values.
    Recibe una ruta de archivo .csv que contenga los precios de venta
    de cada fruta y devuelve un diccionario con los nombres como clave
    y los precios como valores.
    """
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                pass
    return precios


if len(sys.argv) == 2:
    archivo = sys.argv[1]
#elif len(sys.argv) == 3: # Considero el caso usando -i en cmd
#    archivo = sys.argv[2]  # El -i no entra en argv, mala mia
else:
    archivo = 'fecha_camion.csv'
    

# Balance
# Funct calling
camion = leer_camion(archivo)
precios_venta = leer_precios('Data/precios.csv')

total_camion = 0.0 # Calculo el costo de cargar el camion
for fruta in camion:
    total_camion += fruta['cajones'] * fruta['precio']


total_recaudado = 0.0 # Calculo lo recaudado al vender los cajones
for producto in camion:
    total_recaudado += precios_venta[producto['nombre']] * producto['cajones']

diferencia = total_recaudado - total_camion

if diferencia > 0:
    bienomal = 'ganancia'
else:
    bienomal = 'perdida' # si la dif es 0 tambien lo considero perdida

print(f'{"-" * 32}\n{"BALANCE": ^32s}\n{"-" * 32}\n' # printeo tabla
      f'{"Costo total camion": <18s} | ${total_camion: >10,.2f}\n'
      f'{"Total recaudado": <18s} | ${total_recaudado: >10,.2f}\n'
      f'{"Diferencia": <18s} | ${diferencia: >10,.2f}\n'
      f'{"-" * 32}\n\nHubo {bienomal}.')
