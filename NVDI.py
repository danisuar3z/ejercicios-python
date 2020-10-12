# -*- coding: utf8 -*-

# NVDI.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 8.14: Optativo de teledeteccion

import os
import numpy as np
import matplotlib.pyplot as plt

# band1 = np.load('Data/clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band1_clip.npy')

# Idea del companiero Sebastian Zangoni (usar cuantiles como vmin y vmax)

def crear_img_png(carpeta, banda):
    low_q = np.quantile(banda, 0.001)
    high_q = np.quantile(banda, 0.999)
    plt.imshow(banda, vmin=low_q, vmax=high_q)
    plt.colorbar(shrink=0.6)
    plt.savefig(os.path.join(carpeta, 'bandN.png'), dpi=800)
    plt.show()

# No tuve tiempo de ver el resto, estuve con parciales
