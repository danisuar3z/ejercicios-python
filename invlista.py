# busqueda_en_listas.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 3.8: Invertir una lista

def invertir_lista(lista):
    """
    Toma una lista y devuelve otra con los valores invertidos en
    posicion.
    """
    invertida = []
    # Empiezo a contar en 1 para no corregir luego en el append
    for i, e in enumerate(lista, 1):
        invertida.append(lista[-i])
    return invertida

# invertir_lista([0, 1, 2, 3, 4, 5])
# Salida:        [5, 4, 3, 2, 1, 0]

# invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando','San Miguel'])
# Salida:        ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
