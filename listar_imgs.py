# -*- coding: utf8 -*-

# listar_imgs.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 7.5: Recorrer el arbol de archivos

import os
import sys

# No entendi si querian solo el nombre o el full path
# asi que hago ambas con un parametro optativo
# Aclarar que hice algo distinto para usarlo en el otro proyecto
# Quiza podriamos dejar q la salida sea la lista, no los prints

def listar_imgs(folder, full_path=False, silence=False):
    '''
    '''
    imgs = []
    for root, dirs, files in os.walk(folder):
        for name in files:
            if '.png' in name:
                imgs.append(os.path.join(root, name))
                if not silence:
                    if full_path:
                        print(os.path.join(root, name))
                    else:
                        print(name)
    return imgs


def main(argv):
    if len(argv) == 1:
        print('Correct usage: "listar_imgs.py dir_path" or '
                '"listar_imgs.py dir_path full_path" for '
                'full_path=True.')
    elif len(argv) == 2:
        listar_imgs(argv[1])
    elif argv[2] == 'full_path':
        listar_imgs(argv[1], full_path=True)


if __name__ == '__main__':
    main(sys.argv)

