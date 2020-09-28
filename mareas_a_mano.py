# -*- coding: utf8 -*-

# mareas_a_mano.py
# Dani Suarez - suarezdanieltomas@gmail.com

# 7.5: Series temporales
# Analisis y visualizacion de series temporales

# import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data/OBS_SHN_SF-BA.csv',
        index_col=['Time'], 
        parse_dates=True,
)

dh = df['12-25-2014':].copy()
delta_t = -1
delta_h = 18
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
# plt.show()
