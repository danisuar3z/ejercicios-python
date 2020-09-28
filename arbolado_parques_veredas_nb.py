#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[26]:


df_veredas = pd.read_csv('Data/arbolado-lineal.csv')


# In[8]:


df_parques = pd.read_csv('Data/arbolado-en-espacios-verdes.csv')


# In[47]:


df_tipas_parques = df_parques[df_parques.nombre_cie.isin(['Tipuana Tipu'])].copy()


# In[48]:


df_tipas_veredas = df_veredas[df_veredas.nombre_cientifico.isin(['Tipuana tipu'])].copy()


# In[65]:


df_tipas_parques.rename(columns={'altura_tot': 'altura'}, inplace=True)
df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura'}, inplace=True)


# In[55]:


df_tipas_parques['ambiente'] = ['parque']*len(df_tipas_parques)
df_tipas_veredas['ambiente'] = ['vereda']*len(df_tipas_veredas)


# In[69]:


# Me olvide de seleccionar las columnas
df_tipas_parques = df_tipas_parques[['altura', 'diametro', 'ambiente']]
df_tipas_veredas = df_tipas_veredas[['altura', 'diametro', 'ambiente']]


# In[76]:


df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


# In[77]:


df_tipas


# In[79]:


df_tipas.boxplot('diametro', by='ambiente')


# In[80]:


df_tipas.boxplot('altura', by='ambiente')

