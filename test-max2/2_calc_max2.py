# Apr-05-2025
# 2_calc_max2.py

from pathlib import Path
from timer import init_timer, save_elapsed_time_hour_min_sec

from utils import init_directory, remove_directory
from max2.src.get_shapes_distance import get_shapes_distance

path_match_in = Path.cwd() / '_BATCH_FILES' / 'match.txt'
path_mismatch_in = Path.cwd() / '_BATCH_FILES' / 'mismatch.txt'
path_match_out = Path.cwd() / '__RESULTS_max2' / 'result_match_max2.txt'
path_mismatch_out = Path.cwd() / '__RESULTS_max2' / 'result_mismatch_max2.txt'
path_time = Path.cwd() / '__RESULTS_max2' / 'elapsed_time_max2.txt'


def calc_max2():

    # MATCH
    # -------------------------------------------------------------
    print(f'\nM A T C H:')

    # Call function file.readlines() to return a list
    # where each item is a line from file.
    file_in = open(path_match_in, 'r')
    content_list = file_in.readlines()
    file_in.close()

    file_out = open(path_match_out, 'a')

    n_lines = len(content_list)

    for n in range(n_lines):
        line_LF = content_list[n]
        line = line_LF.strip()

        list_temp = line.split('\t')
        count = list_temp[0]
        path_1 = list_temp[1]
        path_2 = list_temp[2]

        distance = get_shapes_distance(path_1, path_2)
        distance_str = str(round(distance, 6))

        str_out = count + '\t\t'
        str_out = str_out + path_1 + '\t\t'
        str_out = str_out + path_2 + '\t\t'
        str_out = str_out + distance_str + '\n'

        file_out.write(str_out)

        print(f'{count}\t\t {path_1}\t\t {path_2}\t\t {distance_str}')

    file_out.close()
    # -------------------------------------------------------------

    # MISMATCH
    # -------------------------------------------------------------
    print(f'\nM I S M A T C H:')

    # Call function file.readlines() to return a list
    # where each item is a line from file.
    file_in = open(path_mismatch_in, 'r')
    content_list = file_in.readlines()
    file_in.close()

    file_out = open(path_mismatch_out, 'a')

    n_lines = len(content_list)

    for n in range(n_lines):
        line_LF = content_list[n]
        line = line_LF.strip()

        list_temp = line.split('\t')
        count = list_temp[0]
        path_1 = list_temp[1]
        path_2 = list_temp[2]

        distance = get_shapes_distance(path_1, path_2)
        distance_str = str(round(distance, 6))

        str_out = count + '\t\t'
        str_out = str_out + path_1 + '\t\t'
        str_out = str_out + path_2 + '\t\t'
        str_out = str_out + distance_str + '\n'

        file_out.write(str_out)

        print(f'{count}\t\t {path_1}\t\t {path_2}\t\t {distance_str}')

    file_out.close()
    # -------------------------------------------------------------


if __name__ == '__main__':

    init_directory('__RESULTS_max2')
    init_directory('TEMP')

    # Calculations
    # -------------------------------------------------------------
    init_timer()

    calc_max2()

    save_elapsed_time_hour_min_sec(path_time)
    # -------------------------------------------------------------

    remove_directory('TEMP')
