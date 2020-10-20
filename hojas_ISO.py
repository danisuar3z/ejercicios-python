# -*- coding: utf8 -*-

# hojas_ISO.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 10.13: Hojas ISO y recursión


def iso_A(N):
    A0 = [841, 1189]
    def iso_(N):
        if N == 0:
            return A0
        if A0[0] < A0[1]:
            A0[1] //= 2
            return iso_(N-1)
        elif A0[0] > A0[1]:
            A0[0] //= 2
            return iso_(N-1)
    return iso_(N)
