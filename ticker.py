# -*- coding: utf-8 -*-

# ticker.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 9.15: Codigo simple

import csv

from vigilante import vigilar
from informe import leer_camion
from formato_tabla import crear_formateador


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    # rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def ticker(camion_file, log_file, fmt):
    fmtter = crear_formateador(fmt)
    headers = ['Nombre', 'Precio', 'Volumen']
    camion = leer_camion(camion_file)
    lines = vigilar(log_file)
    rows = parsear_datos(lines)
    rows = (row for row in rows if row['nombre'] in camion)
    fmtter.encabezado(headers)
    for row in rows:
        fmtter.fila(row.values())


# if __name__ == '__main__':
#     camion = leer_camion('Data/camion.csv')
#     lines = vigilar('Data/mercadolog.csv')
#     rows = parsear_datos(lines)
#     rows = (row for row in rows if row['nombre'] in camion)
#     for row in rows:
#         print(row)

# ticker('Data/camion.csv', 'Data/mercadolog.csv', 'txt')