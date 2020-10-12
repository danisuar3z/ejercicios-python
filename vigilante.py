# -*- coding: utf-8 -*-

# vigilante.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 9.7: Cambios de precio de un camion

import os
import time

from informe import leer_camion

def vigilar(filename):
    f = open('Data/mercadolog.csv')
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        yield line


if __name__ == '__main__':

    camion = leer_camion('Data/camion.csv')

    for line in vigilar('Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')