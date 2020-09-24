# -*- coding: utf-8 -*-

# smilescopy.py
# Daniel T. Suárez - suarezdanieltomas@gmail.com

'''
Este script sirve para extraer el código SMILES isomérico (si lo hay, 
caso contrario el canónico) de PubChem.
'''
import re, pyperclip

# Create SMILES regex 
# TODO: Agregar | Canonical
smiles_regex = re.compile(r'(Isomeric SMILES\tHelpNew Window\r\n){1}'
                     '([CNOH=@\[\]1-9\(\)]){5,300}')

# Create CID regex




# Find matches in clipboard text.
text = str(pyperclip.paste())
smiles = smiles_regex.search(text)
#print(smiles_prueba2.group(0), '\n')

# Export SMILES code
if not smiles:
    print('NO HAY ISOMERIC')
else:
    pyperclip.copy(smiles.group(0)[32:])
    print(pyperclip.paste())    



'''
#%%

# Pruebo con VERBOSE para ver si puedo quedarme fácilmente 
# con el segundo grupo

prueba3 = re.compile(r'(Isomeric SMILES\tHelpNew Window\r\n){1}'
                     '([CNOH=@\[\]1-9\(\)]){5,300}', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
smiles_prueba3 = prueba3.findall(text)
print(smiles_prueba3.group(0), '\n')

# Export SMILES code  
#pyperclip.copy(smiles_prueba3.group(0)[32:])
    
#print(pyperclip.paste())
'''







