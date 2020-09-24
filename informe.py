# -*- coding: utf-8 -*-

# informe_funciones.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.8: Usemos tu módulo


import sys
from fileparse import parse_csv


def leer_camion(nombre_archivo):
    """
    Abre el .csv con la ruta de archivo dada
    y lo "parsea" devolviendo una lista de
    diccionarios para cada fruta en el camión.
    """
    file = open(nombre_archivo, 'rt')
    camion = parse_csv(file, select=['nombre', 'cajones', 'precio'],
                       types=[str, int, float])
    file.close()
    return camion


def leer_precios(nombre_archivo):
    """
    Abre el .csv con la ruta de archivo dada
    y lo "parsea" devolviendo un diccionario
    con los nombres de las frutas como claves
    y los precios de venta como claves.
    """
    file = open(nombre_archivo, 'rt')
    precios = parse_csv(file, has_headers=False, types=[str, float])
    file.close()
    # Convierto la salida de parse_csv a diccionario
    return dict(precios)


def hacer_informe(camion, precios):
    """
    Toma una lista de diccionarios de las frutas
    cargadas en el camion y un diccionario de
    precios y devuelve una lista de tuplas que
    incluye el cambio entre el precio y el costo
    de cada cajon.
    """
    lista_total = []
    for fruta in camion:
        tupla_fruta = (fruta['nombre'], fruta['cajones'],
                       fruta['precio'],
                       (precios[fruta['nombre']] - fruta['precio']))
        lista_total.append(tupla_fruta)
    return lista_total


def imprimir_informe(informe):
    '''
    Recibe un informe y printea una tabla
    para mejor visualización.
    '''
    print(f' {"Fruta":^9} | {"Cajones":^8} | {"Precio":^8} | {"Cambio":^8}')
    print('-'*44)
    for nombre, cajones, precio, cambio in informe:
        print(f' {nombre:<9s} | {cajones:>8d} | '
              f'{"$" + str(f"{precio:.2f}"):>8s} | {cambio:>8.2f} ')


def informe_camion(archivo_camion='Data/camion.csv',
                   archivo_precios='Data/precios.csv'):
    '''
    Llama a las funciones necesarias a partir
    de los nombres de archivo para imprimir
    el informe final. Tiene valores por
    defecto para los archivos.
    '''
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    return imprimir_informe(informe)


def main(argv):
    '''
    Ejecuta el modulo con los parametros
    pasados por la linea de comando.
    '''
    return informe_camion(argv[1], argv[2])


if __name__ == '__main__':
    if len(sys.argv) != 1:
        main(sys.argv)


'''
main(['', 'Data/camion.csv', 'Data/precios.csv'])
print()
main(['', 'Data/missing.csv', 'Data/precios.csv'])
'''
