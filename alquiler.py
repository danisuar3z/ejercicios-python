# -*- coding: utf-8 -*-

# alquiler.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 10.14: precio_alquiler ~ superficie

import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x, y):  # x, y de tipo np.ndarray
    a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean())**2))
    b = y.mean() - a * x.mean()
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
a, b = ajuste_lineal_simple(superficie, alquiler)
errores = alquiler - (a*superficie + b)
# print(errores)
print("ECM:", (errores**2).mean())

grid_x = np.linspace(min(superficie), max(superficie), 5)
grid_y = grid_x * a + b

plt.scatter(superficie, alquiler)
plt.title('precio_alquiler ~ superficie')
plt.xlabel(r'Superficie ($m^{2}$)')  # Uso LaTeX
plt.ylabel('Alquiler (ARS $ / 1000)')

plt.plot(grid_x, grid_y, color='r')