# -*- coding: utf-8 -*-

# costo_camion.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.9: Un poco más allá

import sys
from informe import leer_camion


def costo_camion(nombre_archivo):
    '''
    Calcula y devuelve el costo de cargar 
    un camión a partir de un archivo con 
    la cantidad de cajones y su precio. 
    Utiliza informe_funciones.leer_camion().
    '''
    camion = leer_camion(nombre_archivo)
    return camion.precio_total()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        costo_camion('Data/camion.csv')
    if len(sys.argv) == 2:
        costo_camion(sys.argv[1])