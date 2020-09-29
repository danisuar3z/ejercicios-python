# -*- coding: utf-8 -*-

import pandas as pd

# Creo los DataFrames a partir de los archivos
df_veredas = pd.read_csv('Data/arbolado-lineal.csv')
df_parques = pd.read_csv('Data/arbolado-en-espacios-verdes.csv')

# Me quedo con la especie a analizar (Tipas)
df_tipas_parques = df_parques[
        df_parques.nombre_cie.isin(['Tipuana Tipu'])].copy()

df_tipas_veredas = df_veredas[
        df_veredas.nombre_cientifico.isin(['Tipuana tipu'])].copy()

# Renombro las columnas para que coincidan en nombre
df_tipas_parques.rename(columns={'altura_tot': 'altura'}, inplace=True)
df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro',
                                 'altura_arbol': 'altura'}, inplace=True)

# Agrego columna ambientes para poder concatenar luego
df_tipas_parques['ambiente'] = ['parque']*len(df_tipas_parques)
df_tipas_veredas['ambiente'] = ['vereda']*len(df_tipas_veredas)

# Selecciono columnas deseadas
df_tipas_parques = df_tipas_parques[['altura', 'diametro', 'ambiente']]
df_tipas_veredas = df_tipas_veredas[['altura', 'diametro', 'ambiente']]

# Concateno DataFrames en uno solo
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Observo la magia de pandas
df_tipas

# Boxplot para diametros
df_tipas.boxplot('diametro', by='ambiente')

# Boxplot para alturas
df_tipas.boxplot('altura', by='ambiente')

