# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:25:33 2020

@author: Daniel
"""

"""
Una mañana ponés un billete en la vereda al lado del obelisco porteño. A 
partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos 
prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea más 
alta que el obelisco?

"""

altura_billete = 0.11 / 1000
altura_obelisco = 67.5

num_billetes = 1
dia = 1

while altura_billete * num_billetes <= altura_obelisco:
    num_billetes = num_billetes * 2
    dia+=1
else:
    print("En el dia",dia,"la pila de billetes pasara al obelisco en altura, con un número total de",num_billetes,"billetes")

