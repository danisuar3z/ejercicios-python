# tablamult.py
# Daniel T. Suarez
# Ejercicio 2.34: Tablas de multiplicacion

"""
Me aproveche de una idea de Santiago Menendez en el canal de discord 
para hacer el doble loop, ya que el codigo que yo habia logrado no 
funcionaba para la tabla del cero, ya que usaba range(0,i*9,i) y el 
range no puede tener step = 0
"""

print('-'*44 + f'\n{"Tablas de multiplicacion":^44}\n' + '-'*44)
print('   ',end='')
for i in range(10): # Encabezado
    print(f' {i:3d}',end="")
print('\n'+'-'*44)

for i in range(10):
    print(f'{i}: ', end='')
    num = 0
    for j in range(10): # Tabla del i
        print(f' {num :3}',end='')
        num += i
    print('')
