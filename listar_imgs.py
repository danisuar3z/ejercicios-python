# -*- coding: utf8 -*-

# listar_imgs.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Ejercicio 7.5: Recorrer el arbol de archivos

import os
import sys

# No entendi si querian solo el nombre o el full path
# asi que hago ambas con un parametro optativo

def listar_imgs(folder, full_path=False):
    '''
    Prints the names of all .png pictures in
    the directory given and its subdirectories.
    Prints only the filename by default.
    '''
    for root, dirs, files in os.walk(folder):
        for name in files:
            if '.png' in name:
                if full_path:
                    print(os.path.join(root, name))
                else:
                    print(name)
                    print(os.path.splitext(name))

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

