# -*- coding: utf8 -*-

# ordenar_imgs.py
# Dani Suarez - suarezdanieltomas@gmail.com

'''
EXPLICAR SCRIPT
'''

import os
from datetime import datetime


def process_image(img_path, new_folder):
    '''
    pre: .png or .jpg (not .jpeg), Data folder already exists,
    and new_folder is only the name, without the Data/ part
    '''
    date_ = datetime.strptime(img_path[-12:-4], '%Y%m%d')
    os.utime(img_path, (date_.timestamp(), date_.timestamp()))
    try:
        os.listdir(os.path.join('Data', new_folder))
    except FileNotFoundError:
        os.mkdir(os.path.join('Data', new_folder))
    finally:   
        os.rename(img_path, os.path.join(
            'Data', new_folder, img_path[:-13] + img_path[-4:]))
    return 0

# TODO: Recorrer subcarpetas

def walk_and_process(new_folder):
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name[-3:] in ['png', 'jpg']:
                process_image(os.path.join(
                    root, name), new_folder)
        for name in dirs:




# TODO: Eliminar carpetas vacias



