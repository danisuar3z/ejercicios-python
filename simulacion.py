# -*- coding: utf-8 -*-

# simulacion.py
# Dani Suarez - suarezdanieltomas@gmail.com
# 9.5: Predador Presa

from Data.predador.animal import Leon, Antilope

L = Leon()
L.energia
L.edad
L.es_leon()
L.es_antilope()
L.pasar_un_ciclo()
L.energia
L.edad
L.tiene_hambre()

A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()

vecinos = [(1, A1), (2, A2)]
pos = L.alimentarse(vecinos)

if pos:
    print(f'El leon se come a A{pos}')
else:
    print('El Leon no come.')


M = Leon()
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
L.puede_reproducir()

vecinos = [L]
lugares_libres = [4,5,6,7,8]
L.puede_reproducir()
M.puede_reproducir()

pos = M.reproducirse(vecinos, lugares_libres)
print(f'nace un nuevo leoncito en la posición {pos}')
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()
L.puede_reproducir()
