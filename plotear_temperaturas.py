# -*- coding: utf-8 -*-

# plotear_temperaturas.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 4.14: Empezando a plotear

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('Data/Temperaturas.npy')

plt.hist(temperaturas, bins=30, color='purple')
