# -*- coding: utf8 -*-

# fibonacci_envuelto.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 10.12: Envolviendo a Fibonacci


def fibonacci_wrapped(n):
    """
    Toma un entero positivo n y
    devuelve el n-esimo numero de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-esimo numero de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            # print('ya me lo se:', 'n:', n, 'fibo:',dict_fibo[n])
            F = dict_fibo[n]
        else:
            # print('lo calculo...')
            F = fibonacci_aux(n - 1, dict_fibo) + fibonacci_aux(n - 2, dict_fibo)
            dict_fibo[n] = F
        return F
    
    dict_fibo = {0:0, 1:1}
    F = fibonacci_aux(n, dict_fibo)
    return F 
