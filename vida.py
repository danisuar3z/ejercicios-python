# -*- coding: utf8 -*-

# vida.py
# Dani Suarez - suarezdanieltomas@gmail.com

from datetime import datetime


def seg_vividos(fecha_cumple):
    '''
    pre: recibe una fecha con formato "dd/mm/AAAA"
    pos: devuelve el numero de segundos transcurridos
    desde esa fecha hasta el momento actual.
    '''
    ahora = datetime.now()
    cumple = datetime.strptime(fecha_cumple, '%d/%m/%Y')
    delta = ahora - cumple
    return round(delta.total_seconds())

