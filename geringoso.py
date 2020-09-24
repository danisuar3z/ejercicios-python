# geringoso.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 1.18: Geringoso rustico

cadena = 'Abierto'
vocales = 'aeiou'
capadepenapa = ''

for letra in cadena:
    if vocales.find(letra.lower()) == -1: # Tambien puede ser if letra
        capadepenapa += letra             #                 in vocales:
    else:
        capadepenapa += letra + 'p' + letra.lower()

print(f'{cadena} => {capadepenapa}')
# Salida: "Abierto => Apabipiepertopo"

#%%
# Version entregada

cadena = 'Abierto'
vocales = 'aeiou'
capadepenapa = ''

for letra in cadena:
    if vocales.find(letra.lower()) == -1:
        capadepenapa += letra
    else:
        capadepenapa += letra + 'p' + letra

print(capadepenapa)