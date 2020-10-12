# -*- coding: utf8 -*-

# canguros.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 8.11: Canguros buenos y canguros malos

# Mi clase

class Canguro_mio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido_marsupio = []

    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)

    def __str__(self):
        return f'Canguro; contenido_marsupio = {self.contenido_marsupio}'

    def __repr__(self):
        return f'Canguro({self.nombre})'


# canguro_malo corregido (mal inicializado el atributo contenido_marsupio)

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []

    def __str__(self):
        """devuelve una representacion como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
