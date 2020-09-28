# -*- coding: utf8 -*-

# arbolado_parques_veredas.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 7.7: Lectura y selección

# import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('Data/arbolado-lineal.csv')
# Arma un DataFrame que tenga solamente las siguiente columnas
cols = [
  'nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol',
]
# Trabajaremos con las siguientes especies seleccionadas
especies = [
    'Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu',
]

df = df[cols]

# Imprimi las diez especies mas frecuentes con sus respectivas cantidades.
print(df.nombre_cientifico.value_counts().head(10))

# Selecciono especies
df = df[df.nombre_cientifico.isin(especies)]

# %%
df.boxplot('diametro_altura_pecho', by='nombre_cientifico')
# plt.show()
# %%
df.boxplot('altura_arbol', by = 'nombre_cientifico')
# plt.show()
# %%
sns.pairplot(data=df, hue='nombre_cientifico')
# plt.show()
# %%
dtypes_parques = {
    0:'float64', 1:'float64', 2:'int64', 3:'int64', 4:'int64', 5:'int64', 
    6:'int64', 7:'str', 8:'str', 9:'str', 10:'str', 11:'str', 12:'str', 
    13:'str', 14:'str', 15:'float64', 16:'float64',
}

dtypes_veredas = {
    'float', 
}

df_parques = pd.read_csv(
    'Data/arbolado-en-espacios-verdes.csv', dtype=dtypes_parques)
df_veredas = pd.read_csv('Data/arbolado-lineal.csv', dtypes=dtypes_veredas)

df_tipas_parques = df_parques[df_parques.nombre_cientifico == 'Tipuana Tipu']
df_tipas_veredas = df_veredas[df_parques.nombre_cie == 'Tipuana tipu']











