# Apr-05-2025
# draw_result.py

import cv2 as cv

from max2.src import cfg
from max2.src.draw_utils import draw_peak, draw_text


def draw_result(tag, list_of_peaks):

    path_in = cfg.dir_debug + '/' + tag + '.png'
    magn = cv.imread(path_in, cv.IMREAD_UNCHANGED)

    # Draw line
    # -----------------------------------------
    x1 = cfg.X0
    y1 = cfg.Y0
    x2: int = 0
    y2: int = 0

    if tag == 'image':
        x2 = int(cfg.x_src)
        y2 = int(cfg.y_src)

    if tag == 'templ':
        x2 = int(cfg.x_dst)
        y2 = int(cfg.y_dst)

    thickness = 2
    cv.line(magn,
            (x1, y1),
            (x2, y2),
            cfg.cayenne, thickness)


    # Draw peaks
    # -----------------------------------------
    n = 0
    for item in list_of_peaks:
        y = int(item[0])
        x = int(item[1])
        draw_peak(magn, x, y, cfg.dark_gray, 2, -1)
        if n > 0:
            draw_text(magn, x + 5, y + 0, cfg.black, str(n))
        else:
            draw_text(magn, x - 7, y + 23, cfg.black, str(n))
        n += 1
    # -----------------------------------------

    path_out = cfg.dir_debug + '/' + tag + '_result.png'
    cv.imwrite(path_out, magn)
