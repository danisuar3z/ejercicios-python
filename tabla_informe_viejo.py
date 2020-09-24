# tabla_informe.py
# Daniel T. Suarez
# Ejercicio 2.33: Un desafio de formato
# Ejercicio 6.2: Funcion main()

import csv


def leer_camion(nombre_archivo):
    """
    Recibe una ruta de archivo .csv que contenga los datos de carga
    de un camion de frutas y devuelve una lista de diccionarios con
    toda la informacion de cada fruta.
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


def hacer_informe(camion, precios):
    """
    Toma una lista de diccionarios de las frutas cargadas en el camion
    y un diccionario de precios y devuelve una lista de tuplas que
    incluye el cambio entre el precio y el costo de cada cajon.
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
    '''
    return informe_camion(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
    
'''
informe_camion()
print()
informe_camion(archivo_camion='Data/missing.csv')
'''
