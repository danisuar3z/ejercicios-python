# -*- coding: utf-8 -*-

# informe_funciones.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 2.6: Missing (try except para valores faltantes)
# Ejercicio 5.9: Un poco más allá


def costo_camion(archivo):

    f = open(archivo)
    next(f)
    
    cajones = []
    precio = []
    
    for line in f:
        row = line.split(',')
        try:
            cajones.append(int(row[1]))
            precio.append(float(row[2].replace('\n','')))
        except ValueError:
            pass
        
    costo_total = 0
    
    for i in range(len(cajones)):
        costo_total += cajones[i]*precio[i]

    f.close()
    return costo_total

costo = costo_camion('Data/missing.csv')
print(f'Costo total: ${costo}')


#%%
# Ej 2.5: Como lo pidieron ellos
def costo_camion(archivo):

    f = open(archivo)
    next(f)
    
    cajones = []
    precio = []
    
    for line in f:
        row = line.split(',')
        cajones.append(int(row[1]))
        precio.append(float(row[2].replace('\n','')))
    
    costo_total = 0
    
    for i in range(len(cajones)):
        costo_total += cajones[i]*precio[i]

    f.close()
    return costo_total

costo = costo_camion('Data/camion.csv')
print(f'Costo total: ${costo}')


#%%
# Ej 2.5: Con input y try except para la carga del archivo
def costo_camion():
    valido = False
    while not valido:
        try:
            archivo = input('Ingrese el nombre del archivo y subcarpetas de ser necesario:\n\n')
            f = open(archivo)
            next(f)
            
            cajones = []
            precio = []
            
            for line in f:
                row = line.split(',')
                cajones.append(int(row[1]))
                precio.append(float(row[2].replace('\n','')))
            
            costo_total = 0
            
            for i in range(len(cajones)):
                costo_total += cajones[i]*precio[i]
            
            valido = True
            f.close()
            return f'Costo total: ${costo_total:,}'
        except FileNotFoundError:
            print('No se encontro el archivo.')

salida = costo_camion()
print(salida)
#%%