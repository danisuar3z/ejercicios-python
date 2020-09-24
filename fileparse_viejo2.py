# -*- coding: utf-8 -*-

# fileparse.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 6.4: De archivos a "objetos cual archivos"

import csv

def parse_csv(objeto, select=None, types=None, 
              headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV u objeto en una lista de 
    registros.
    Saltea líneas vacías y salva ValueError al 
    intentar convertir los tipos de datos.
    '''
    # Atrapo error al pedir select sin headers
    if select and not headers:
        raise RuntimeError('Que queres seleccionar sin headers?')
    filas = csv.reader(objeto)
    if not headers: # headers=False
        registros = []
        for fila in filas:
            if not fila:
                continue
            tupla_cosas = ()
            for cosa in fila:
                tupla_cosas += (cosa,)
            registros.append(tupla_cosas)
    else:    # headers = True
        # Leo los encabezados del archivo
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(ncolumna) for ncolumna in select]
            # Me quedo solo con los encabezados que me interesan
            encabezados = select
        else:
            indices = []

        registros = []
        for i, fila in enumerate(filas, 1):
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                if types:
                    try:    # Salvo si hay errores/blancos
                        fila = [func(fila[index]) for 
                            index, func in zip(indices, types)]
                    except ValueError:
                        if not silence_errors:
                            print(f'parse_csv Warning: Error en línea {i}. '
                              f'"{fila}"')
                        continue    # Salteo la fila errónea
                else:
                    fila = [fila[index] for index in indices]
            else:    
                if types:
                    try:
                        fila = [func(fila[j]) for 
                                j, func in enumerate(types)]
                    except ValueError:
                        if not silence_errors:
                            print(f'parse_csv Warning: Error en línea {i}. '
                                  f'"{fila}"')
                        continue    # Salteo la fila errónea
            
            # Si no entró en ningún condicional 
            # entonces fila queda = que antes

            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

#%%
'''
camion = parse_csv('Data/precios.csv', headers=False)
                   #selec=['nombre', 'cajones', 'precio'], 
                   #types=[str, int, float])
print(camion)
'''