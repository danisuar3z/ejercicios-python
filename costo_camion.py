# -*- coding: utf-8 -*-

# costo_camion.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 5.9: Un poco más allá

from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    '''
    Calcula y devuelve el costo de cargar 
    un camión a partir de un archivo con 
    la cantidad de cajones y su precio. 
    Utiliza informe_funciones.leer_camion().
    '''
    camion = leer_camion(nombre_archivo)
    costo = 0
    for fruta in camion:
        costo += fruta['cajones'] * fruta['precio']
    return costo

def main(argv):
    '''
    '''
    return costo_camion(argv[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)