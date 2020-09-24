# enproceso.py
import csv
#from pprint import pprint

archivo = 'Data/enproceso.csv'
lista_meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN',
               'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
lista_nros = ['01', '02', '03', '04', '05', '06', '07', '08',
              '09', '10', '11', '12']
meses = dict(zip(lista_nros, lista_meses))

f = open(archivo, 'rt', encoding='utf8')
rows = csv.reader(f)
headers = next(rows)
for i, header in enumerate(headers):
    headers[i] = headers[i].replace('\xa0', '')
    if i in list(range(1,6)):
        headers[i] = headers[i].replace(' ', '')
    
usuarios = []
for row in rows:
    usuario = dict(zip(headers, row))
    usuario['Nombre'] = usuario['Nombre'].replace('\xa0','')
    mes_unido = usuario['Unido'][5:7]
    usuario['Unido'] = usuario['Unido'][:5] + usuario[
        'Unido'][5:7].replace(mes_unido, meses[mes_unido]) + usuario[
            'Unido'][7:]
    ult_men = usuario['Último mensaje'][5:7]
    usuario['Último mensaje'] = usuario['Último mensaje'][:5] + usuario[
        'Último mensaje'][5:7].replace(ult_men, meses[ult_men]) + usuario[
            'Último mensaje'][7:]
    usuarios.append(usuario)
f.close()
#pprint(usuarios)
#%%
# Print tabla
for header in headers:
    if header in ['Nombre']:
        print(f' {header:^17} |', end='')
    elif header in ['Unido', 'Último mensaje']:
        print(f' {header:^15} |', end='')
    else:
        print(f' {header:^6} |', end='')
print('\n'+'-'*105)
for usuario in usuarios:
    for key in usuario.keys():
        if key in ['Nombre']:
            print(f' {usuario[key]:<17} |', end='')
        elif key in ['Unido', 'Último mensaje']:
            print(f' {usuario[key]:^15} |', end='')
        else:
            print(f' {usuario[key]:>6} |', end='')
    print('')
