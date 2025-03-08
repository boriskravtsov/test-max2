# Mar-08-2025
# draw_peaks.py

import cv2 as cv

from max2.src import cfg_max2
from max2.src.draw_utils import draw_peak, draw_text


def draw_peaks(tag, list_of_peaks):

    path_in = cfg_max2.dir_debug + '/' + tag + '.png'
    magn = cv.imread(path_in, cv.IMREAD_UNCHANGED)

    # Draw peaks
    # -----------------------------------------
    n = 0
    for item in list_of_peaks:
        y = int(item[0])
        x = int(item[1])
        draw_peak(magn, x, y, cfg_max2.black, 2, -1)
        if n > 0:
            draw_text(magn, x + 5, y + 0, cfg_max2.black, str(n))
        else:
            draw_text(magn, x - 7, y + 23, cfg_max2.black, str(n))
        n += 1
    # -----------------------------------------

    path_out = cfg_max2.dir_debug + '/' + tag + '_peaks.png'
    cv.imwrite(path_out, magn)
