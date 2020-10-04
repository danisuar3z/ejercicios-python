# -*- coding: utf-8 -*-

# lote.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 8.9: Mejor salida para objetos


class Lote:
    '''
    Clase Lote, requiere nombre (str), cantidad
    de cajones (int) y precio del cajon (float).
    '''
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cant):
        self.cajones -= cant

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
    def __str__(self):
        return f'({self.nombre}, {self.cajones}, {self.precio})'
