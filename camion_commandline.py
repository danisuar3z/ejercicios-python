# camion_commandline.py
# Daniel T. Suarez
# Ejercicio 2.8: Ejecucion desde la linea de comandos con parametros

import csv
import sys

def costo_camion(nombre_archivo):
    """
    Lee archivo .csv con la informacion de los cajones en un camion
    y su costo, devolviendo el costo total del camion.
    """
    f = open(nombre_archivo)
    headers = next(f).split(',')
    headers[-1] = headers[-1].replace('\n','') # Le saco el caracter \n
    rows = csv.reader(f)

    costo_total = 0    
    for i, row in enumerate(rows, 1):
        try:
            registro = dict(zip(headers, row))
            icajones = int(registro['cajones'])
            iprecio = float(registro['precio'])
            costo_total += icajones * iprecio
        except ValueError:
            print(f'Error en linea {i}: No se puede interpretar '
                  f'{row}')
    f.close()
    return costo_total

# Para elegir el archivo desde la linea de comandos
if len(sys.argv) == 2:
    archivo = sys.argv[1]
elif len(sys.argv) == 3: # Considero el caso usando -i en cmd
    archivo = sys.argv[2]
else:
    archivo = 'Data/fecha_camion.csv'

print(f'Costo total: ${costo_camion(archivo):,}')
# Salida: Costo total: $47,671.15
