# esfera.py
# Daniel T. Su√°rez - suarezdanieltomas@gmail.com
# Ejercicio 1.13: El volumen de una esfera


import math

radio = 'a' # Le doy un valor de not digit para que el bool del while sea True

while not radio.isdigit(): # Para que vuelva a pedir input si el usuario pone letras
    radio = input('Ingrese el radio de la esfera en metros:\n')
    try:
        r = float(radio)
        volumen = 4/3*math.pi*r**3
        print('El volumen de una esfera de {}m de radio es {}m\u00B3.'
          .format(radio,round(volumen, 1)))
    except:
        print('Solo numeros por favor.')

# Salida: 'El volumen de una esfera de 6m de radio es 904.8 m≥.'
