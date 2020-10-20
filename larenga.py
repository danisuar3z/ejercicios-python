# -*- coding: utf8 -*-

# larenga.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 10.9: Pascal


def pascal(n, k):
    if n == 0:
        return 1
    if k == 0:
        return 1
    if k == n:
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)

# print(pascal(5, 2))
# Out: 10
