# -*- coding: utf8 -*-

# ordenar_imgs.py
# Dani Suarez - suarezdanieltomas@gmail.com

'''
EXPLICAR SCRIPT
'''

import sys
import os
from datetime import datetime


def process_image(img_path, new_folder, root):
    '''
    pre: .png or .jpg (not .jpeg), Data folder already exists,
    and new_folder is only the name, without the Data/ part.
    date in YYYYMMDD format before the format extention.
    pos:
    '''
    date_ = datetime.strptime(img_path[-12:-4], '%Y%m%d')
    os.utime(img_path, (date_.timestamp(), date_.timestamp()))
    os.rename(img_path, os.path.join(
        'Data', new_folder, img_path[:-13].replace(root, '.') + img_path[-4:]))


def walk_and_process(new_folder):
    for root, dirs, files in os.walk('.', topdown=True):
        dirs[:] = [d for d in dirs if d != 'Data']
        for name in files:
            if name[-3:] in ['png', 'jpg']:
                process_image(os.path.join(
                    root, name), new_folder, root)


def delete_empty_dirs():
    for root, _, _ in os.walk('.', topdown=False):
        if root == '.':
            break
        try:
            os.rmdir(root)
        except OSError:
            pass
    return


def setup_dirs(new_folder):
    # Create Data Folder
    try:
        os.mkdir('Data')
        os.mkdir(os.path.join('Data', new_folder))
    except FileExistsError:
        raise RuntimeError(f'Directory ("Data" or "{new_folder}") already '
                           'exists, if you want to process a folder with '
                           'that name, the script needs to be changed.\n'
                           'If you don\'t want this dirs to be processed, '
                           'set setup_not_needed=True in main function.')



def main(argv, setup_not_needed=False):
    if not setup_not_needed:
        setup_dirs('cacona')
    walk_and_process('cacona')
    delete_empty_dirs()

if __name__ == '__main__':
    main(sys.argv)

