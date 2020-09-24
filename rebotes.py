# rebotes.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 1.5: La pelota que rebota

altura = 100
i=1

while i <= 10:
    altura = altura * 3/5
    print(i, round(altura, 2))
    i += 1
