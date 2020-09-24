# inclusive.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com
# Ejercicio 1.29: Traductor al lenguaje inclusivo

frase = 'todos somos programadores'
lista_frase = frase.split(' ')
lista_frese = []

for palabra in lista_frase:
    if ',' in palabra: # Para solucionar el caso de las comas. Deberia volver a
        palabra = palabra.replace(',', '') # agregarla a lo ultimo pero quedaria 
    if len(palabra) <2:                    # un choclo el codigo
        lista_frese.append(palabra)        
    elif palabra[-2] == 'o':
        lista_frese.append(palabra[:-2] + 'e' + palabra[-1])
    elif palabra[-1] == 'o':
        lista_frese.append(palabra[:-1] + 'e')
    else:
        lista_frese.append(palabra)

frese = ' '.join(lista_frese)
print(frese)
