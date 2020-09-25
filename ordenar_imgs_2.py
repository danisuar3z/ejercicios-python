# -*- coding: utf8 -*-

# ordenar_imgs.py
# Dani Suarez - suarezdanieltomas@gmail.com

'''
EXPLICAR SCRIPT
'''

import os
from datetime import datetime

from listar_imgs import listar_imgs # Change to list_imgs


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


def process_folder(new_folder):
    imgs_list = listar_imgs('.', silence=True)
    for img in imgs_list:
        process_image(img, new_folder)
    return 0


def delete_empty_folders(dircty='.'):
    # Tengo q pensarlo aun
    return


