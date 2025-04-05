# Apr-05-2025
# create_table.py

import sys
import numpy as np
from numpy import ndarray
import math

from max2.src import cfg
from max2.src.get_angle import get_angle_axe_x

"""
table columns:
0:  x       - абсцисса в системе координат изображения.
1:  y       - ордината в системе координат изображения.
2:  length  - длина вектора  
3:  angle   - угол между вектором и осью X в централизованной системе координат.
"""


def create_table(list_of_peaks) -> ndarray:

    first = list_of_peaks[0]
    y_peaks_0 = first[0]
    x_peaks_0 = first[1]

    if y_peaks_0 != cfg.Y0 or x_peaks_0 != cfg.X0:
        print(f'\ncreate_table: Something is going wrong!')
        sys.exit(1)

    table_rows = len(list_of_peaks)
    table_cols = 4

    table = np.zeros((table_rows, table_cols), dtype=np.float32)

    for n in range(table_rows):

        peak = list_of_peaks[n]
        y_peak = peak[0]
        x_peak = peak[1]

        # coordinates
        table[n, 0] = x_peak
        table[n, 1] = y_peak

        # length
        dx: float = x_peak - cfg.X0
        dy: float = y_peak - cfg.Y0
        table[n, 2] = math.sqrt((dx * dx) + (dy * dy))

        # angle
        table[n, 3] = get_angle_axe_x(x_peak, y_peak)

    return table
