# Apr-05-2025
# 4_histogram_max2.py

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

hist_title = 'max2:  3-pointed stars  &  4-pointed stars'

# File names
# -------------------------------------------------------------
path_match = Path.cwd() / '__RESULTS_max2' / 'result_match_max2.txt'
path_mismatch = Path.cwd() / '__RESULTS_max2' / 'result_mismatch_max2.txt'
# -------------------------------------------------------------

#   M A T C H
# -------------------------------------------------------------
line_count_match = len(open(path_match).readlines())

arr_match = np.zeros(line_count_match, dtype='float32')

file_in = open(path_match, 'r')

n = 0

while True:
    line_LF = file_in.readline()

    line = line_LF.strip()

    if line != '':
        list_temp = line.split('\t\t')

        distance = float(list_temp[3])

        arr_match[n] = distance
        n += 1

    if not line:
        break

file_in.close()

arr_match_max = arr_match.max()
# -------------------------------------------------------------

#   M I S M A T C H
# -------------------------------------------------------------
line_count_mismatch = len(open(path_mismatch).readlines())

arr_mismatch = np.zeros(line_count_mismatch, dtype='float32')

file_in = open(path_mismatch, 'r')

n = 0

while True:
    line_LF = file_in.readline()

    line = line_LF.strip()

    if line != '':
        list_temp = line.split('\t\t')

        distance = float(list_temp[3])

        arr_mismatch[n] = distance
        n += 1

    if not line:
        break

file_in.close()

arr_mismatch_min = arr_mismatch.min()
# -------------------------------------------------------------

#   H I S T O G R A M
# -------------------------------------------------------------
# plt.figure(figsize=(5.0, 4.0), dpi=100)
# plt.figure(figsize=(7.0, 5.0), dpi=100)
plt.figure(figsize=(8.0, 5.0), dpi=100)

bins = np.linspace(arr_mismatch_min, arr_match_max, 24)

plt.title(hist_title, fontsize=12)

plt.hist([arr_mismatch, arr_match], bins, label=['mismatch', 'match'])

plt.xlabel('Distance', fontsize=10)
plt.ylabel('Frequency', fontsize=10)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.legend(loc='upper right')

path_hist = '__RESULTS_max2/HISTOGRAM_max2.png'
plt.savefig(path_hist, dpi=150)
# -------------------------------------------------------------

print(f'\nDone')
