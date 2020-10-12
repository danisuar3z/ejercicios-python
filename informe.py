# -*- coding: utf-8 -*-

# informe_funciones.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.8: Usemos tu módulo

import sys

from fileparse import parse_csv
from lote import Lote
from camion import Camion
import formato_tabla


def leer_camion(nombre_archivo):
    """
    Abre el .csv con la ruta de archivo dada
    y lo "parsea" devolviendo una lista de
    objetos Lote para cada fruta en el camión.
    """
    with open(nombre_archivo, 'rt') as f:
        camion_dicts = parse_csv(f, select=['nombre', 'cajones', 'precio'],
                           types=[str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio'])
              for d in camion_dicts]

    return Camion(camion)


def leer_precios(nombre_archivo):
    """
    Abre el .csv con la ruta de archivo dada
    y lo "parsea" devolviendo un diccionario
    con los nombres de las frutas como claves
    y los precios de venta como claves.
    """
    with open(nombre_archivo, 'rt') as f:
        precios = parse_csv(f, has_headers=False, types=[str, float])

    return dict(precios)


def hacer_informe(camion, precios):
    """
    Toma una lista de objetos Lote de las frutas
    cargadas en el camion y un diccionario de
    precios y devuelve una lista de tuplas que
    incluye el cambio entre el precio y el costo
    de cada cajon.
    """
    lista_total = []
    for fruta in camion:
        tupla_fruta = (fruta.nombre, fruta.cajones,
                       fruta.precio,
                       (precios[fruta.nombre] - fruta.precio))
        lista_total.append(tupla_fruta)
    return lista_total


def imprimir_informe(informe, formateador):
    '''
    Recibe un informe y printea una tabla
    para mejor visualización utilizando un
    formateador de la clase FormatoTabla.
    '''
    formateador.encabezado(['Fruta', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, formato='txt'):
    '''
    Llama a las funciones necesarias a partir
    de los nombres de archivo para imprimir
    el informe final.
    '''
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    formateador = formato_tabla.crear_formateador(formato)
    imprimir_informe(informe, formateador)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        informe_camion(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4:
        informe_camion(sys.argv[1], sys.argv[2], sys.argv[3])
    if len(sys.argv) == 1:
        informe_camion('Data/camion.csv', 'Data/precios.csv')
