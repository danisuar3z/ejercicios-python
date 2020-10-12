# -*- coding: utf8 -*-

# camion.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 9.2: Iteracion sobre objetos


class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, item):
        return any(lote.nombre == item for lote in self._lotes)

    def __repr__(self):
        return 'Camion()'

    def __str__(self):
        return f'{"*"+(chr(10)+"*").join(str(lote) for lote in self._lotes)}'

    def precio_total(self):
        return sum(l.costo() for l in self._lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

