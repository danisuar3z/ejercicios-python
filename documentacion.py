# -*- coding: utf-8 -*-

# documentacion.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 6.8: Funciones y documentación


def valor_absoluto(num):
    '''
    Devuelve el valor absoluto (modulo) de
    un numero.
    pre: num dentro de los Reales
    pos: valor absoluto del num
    '''
    if num >= 0:
        return num
    else:
        return -num


def suma_pares(lista):
    '''
    Toma una lista y devuelve la suma de los
    numeros pares presentes en la misma.
    pre: los elementos de la lista deben
    ser numeros
    pos: devuelve la suma de los pares
    '''
    suma = 0
    for e in lista:
        if e % 2 == 0:
            suma += e
        else:
            suma += 0
    return suma


def veces(a, b):
    '''
    Multiplicacion de numeros enteros.
    pre: a, b enteros
    pos: resultado de a*b
    '''
    mult = 0
    nb = b
    while nb != 0:
        print(nb * a)
        mult += a
        nb -= 1
    return mult
# Invar.: nb? no aporta mucho, es una multiplicacion de enteros


def collatz(num):
    '''
    Esta funcion se basa en la conjetura de Collatz
    y realiza la operacion de dividir por 2 si es
    par o multiplicar por 3 y sumar 1 si no lo es.
    pre: num entero >= 1
    pos: numero de veces que se repite el ciclo
    hasta que num = 1.
    ACLARACION: la variable ingresada se modifica.
    '''
    reps = 1
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = 3*num + 1
        reps += 1
    return reps
