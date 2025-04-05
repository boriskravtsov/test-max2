# Apr-05-2025
# 1_create_batch_files.py

import os
import shutil
from pathlib import Path

from utils import init_directory, remove_directory, print_list


def create_batch_files(dir_a, dir_b):

    origin_a = dir_a + '/'
    origin_b = dir_b + '/'

    target = 'TEMP/'

    files = os.listdir(origin_a)
    for file_name in files:
        shutil.copy(origin_a + file_name, target + file_name)

    files = os.listdir(origin_b)
    for file_name in files:
        shutil.copy(origin_b + file_name, target + file_name)

    # Create 2 lists (list_a and list_b) of input data
    # -------------------------------------------------------------
    list_a = []
    for f in os.listdir(dir_a):

        # to escape hidden files
        if f[0] == '.':
            continue

        list_a.append(origin_a + f)

    list_a.sort()
    n_images_a = len(list_a)
    # -------------------------------------------------------------
    list_b = []
    for f in os.listdir(dir_b):

        # to escape hidden files
        if f[0] == '.':
            continue

        list_b.append(origin_b + f)

    list_b.sort()
    n_images_b = len(list_b)
    # -------------------------------------------------------------
    # print_list('list_a:', list_a)
    # print_list('list_b:', list_b)
    # -------------------------------------------------------------

    # Create MATCH batch file
    # -------------------------------------------------------------
    list_match = []

    count = 1
    for j in range(n_images_a):
        for i in range(j + 1, n_images_a):
            name_1 = list_a[j]
            name_2 = list_a[i]

            record = str(count) + '\t' + name_1 + '\t' + name_2

            list_match.append(record)

            count += 1

    for j in range(n_images_b):
        for i in range(j + 1, n_images_b):
            name_1 = list_b[j]
            name_2 = list_b[i]

            record = str(count) + '\t' + name_1 + '\t' + name_2

            list_match.append(record)

            count += 1

    save_match(list_match)
    # -------------------------------------------------------------

    # Create MISMATCH batch file
    # -------------------------------------------------------------
    list_mismatch = []

    count = 1
    for j in range(n_images_a):
        for i in range(n_images_b):
            name_a = list_a[j]
            name_b = list_b[i]

            record = str(count) + '\t' + name_a + '\t' + name_b

            list_mismatch.append(record)

            count += 1

    save_mismatch(list_mismatch)
    # -------------------------------------------------------------

    print(f'\nDone')


def save_match(list_match):

    path_match = Path.cwd() / '_BATCH_FILES' / 'match.txt'

    n_records = len(list_match)

    with open(path_match, 'w') as f:
        for n in range(n_records):
            f.write(list_match[n] + '\n')


def save_mismatch(list_mismatch):

    path_mismatch = Path.cwd() / '_BATCH_FILES' / 'mismatch.txt'

    n_records = len(list_mismatch)

    with open(path_mismatch, 'w') as f:
        for n in range(n_records):
            f.write(list_mismatch[n] + '\n')


if __name__ == '__main__':
    init_directory('_BATCH_FILES')
    init_directory('TEMP')

    # Place data in existing directories _DATA_1 and _DATA_2
    create_batch_files('_DATA_1', '_DATA_2')

    remove_directory('TEMP')
