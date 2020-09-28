# -*- coding: utf8 -*-

# mareas_fft.py
# Dani Suarez - suarezdanieltomas@gmail.com

# 7.5: Series temporales
# Analisis y visualizacion de series temporales

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal


def calcular_fft(y, freq_sample = 24.0):
    '''y debe ser un vector con numeros reales
    representando datos de una serie temporal.
    freq_sampleo esta seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sample)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


df = pd.read_csv('Data/OBS_SHN_SF-BA.csv',
        index_col=['Time'], 
        parse_dates=True,
)

inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

freq_sf, fft_sf = calcular_fft(alturas_sf)

plt.plot(freq_sf, np.abs(fft_sf), color='b')
plt.xlabel('Freq')
plt.ylabel('Potencia (energy)')
plt.xlim(0, 4)
plt.ylim(0, 20)
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence=8)[0][-1]
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor='r')
plt.title('Espectro de potencias SF')
plt.show()

ang_sf = np.angle(fft_sf)[pico_sf]
1.48487

freq_ba, fft_ba = calcular_fft(alturas_ba)
plt.plot(freq_ba, np.abs(fft_ba), color='b')
plt.xlabel('Freq')
plt.ylabel('Potencia (energy)')
plt.xlim(0, 4)
plt.ylim(0, 20)
pico_ba = signal.find_peaks(np.abs(fft_ba), prominence=8)[0][-1]
plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor='r')
plt.title('Espectro de potencias Bs. As.')
plt.show()

delta_h = np.abs(fft_sf[0]) - np.abs(fft_ba[0])

ang_ba = np.angle(fft_ba)[pico_ba]
# 1.96351

freq = freq_ba[pico_ba]
ang2h = 24 / (2*np.pi*freq)

retardo = (ang_ba - ang_sf) * ang2h

