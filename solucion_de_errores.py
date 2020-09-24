# solucion_de_errores.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicios de errores en el código

# Ejercicio 3.1: Semántica
# El error era de comportamiento
# Lo corregi cambiando el return False fuera del loop

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))                       # Salida: False
print(tiene_a('abracadabra'))                      # Salida: True
print(tiene_a('La novela 1984 de George Orwell'))  # Salida: True
#%%

# Ejercicio 3.2: Sintaxis
# Errores de Sintaxis y de Name por error de tipeo en False
# Agregue los 3 ":" y el doble =, y cambie el Falso por False

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))                       # Saliad: False
print(tiene_a('La novela 1984 de George Orwell'))  # Salida: True
#%%

# Ejercicio 3.3: Tipos
# TypeError al ingresar valores que no sean cadenas
# Lo solucione convirtiendo la entrada a string al principio

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))                       # Salida: True
print(tiene_uno('La novela 1984 de George Orwell'))  # Salida: True
print(tiene_uno(1984))                               # Salida: True
#%%

# Ejercicio 3.4: Alcances
# La funcion no tiene return por lo que no se puede usar c fuera de ella
# Lo solucione agregando el return

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}") # Salida: La suma da 2 + 3 = 5
#%%

# Ejercicio 3.5: Pisando memoria
# Las listas no guardan valores sino sus direcciones, y al cambiar los
# valores del diccionario, se actualizan en la lista tambien
# Lo solucione moviendo registro = {} dentro del loop

import csv
from pprint import pprint
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)

'''
Salida:
[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
 {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
'''


