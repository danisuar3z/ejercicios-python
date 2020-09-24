# -*- coding: utf-8 -*-

# termometro.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 4.11: Gaussiana

import random
import numpy as np

# Termómetro

n = 999
temp = 37.5
medidas = [temp + random.normalvariate(0, 0.2) for i in range(n)]
medidas.sort() # Para obtener la mediana por posición fácilmente

maximo = max(medidas)
minimo = min(medidas)
promedio = sum(medidas)/n
mediana = medidas[n//2]
cuartil_25 = medidas[int(n//4)]


print(medidas)
print(f'\nValor máximo:---{maximo:.2f} °C\n'
      f'Valor mínimo:---{minimo:.2f} °C\n'
      f'Promedio:-------{promedio:.2f} °C\n'
      f'Mediana:--------{mediana:.2f} °C\n'
      f'Cuartil 0.25:---{cuartil_25:.2f} °C\n')

# No recuerdo la convención para los cuartiles, si se considera el 
# número entero anterior o el siguiente (998/4 = 249.5)

#%%

# Ejercicio 4.13: Guardar temperaturas

# Exporto el vector

np.save('Data/Temperaturas', medidas)

