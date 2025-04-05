# Apr-05-2025
# 3_sort_max2.py

import numpy as np
from pathlib import Path

from shell_sort import shell_sort_increase, shell_sort_decrease

path_match_sort_in = Path.cwd() / '__RESULTS_max2' / 'result_match_max2.txt'
path_match_sort_out = Path.cwd() / '__RESULTS_max2' / 'result_match_sort_max2.txt'
path_mismatch_sort_in = Path.cwd() / '__RESULTS_max2' / 'result_mismatch_max2.txt'
path_mismatch_sort_out = Path.cwd() / '__RESULTS_max2' / 'result_mismatch_sort_max2.txt'


def sort_result_match(path_in, path_out):

    # Call function file.readlines() to return a list
    # where each item is a line from file.
    file_in = open(path_in, 'r')
    content_list = file_in.readlines()
    file_in.close()

    n_lines = len(content_list)
    arr_distance = np.zeros(n_lines, dtype='float32')

    for n in range(n_lines):
        line = content_list[n]

        list_temp = line.split('\t\t')
        # line_tag = list_temp[0]
        # filename_1 = list_temp[1]
        # filename_2 = list_temp[2]
        distance = list_temp[3]

        arr_distance[n] = float(distance)

    # Сортировка по величине distance.
    order = np.arange(n_lines)
    shell_sort_increase(arr_distance, order, n_lines)

    file_out = open(path_out, 'a')

    for n in range(n_lines):

        index = order[n]

        line = content_list[index]

        file_out.write(line)

    file_out.close()


def sort_result_mismatch(path_in, path_out):

    # Call file.readlines() to return a list
    # where each item is a line from file.
    file_in = open(path_in, 'r')
    content_list = file_in.readlines()
    file_in.close()

    n_lines = len(content_list)
    arr_distance = np.zeros(n_lines, dtype='float32')

    for n in range(n_lines):
        line = content_list[n]

        list_temp = line.split('\t\t')
        # line_tag = list_temp[0]
        # filename_1 = list_temp[1]
        # filename_2 = list_temp[2]
        distance = list_temp[3]

        arr_distance[n] = float(distance)

    # Сортировка по величине distance.
    order = np.arange(n_lines)
    shell_sort_decrease(arr_distance, order, n_lines)

    file_out = open(path_out, 'a')

    for n in range(n_lines):

        index = order[n]

        line = content_list[index]

        file_out.write(line)

    file_out.close()


if __name__ == '__main__':

    sort_result_match(path_match_sort_in, path_match_sort_out)
    sort_result_mismatch(path_mismatch_sort_in, path_mismatch_sort_out)

    print(f'\nDone')
