# Feb-13-2025
# draw_result.py

import cv2 as cv

from max2.src import cfg_max2


def draw_result(tag):

    path_in = cfg_max2.dir_debug + '/' + tag + '_peaks.png'
    magn = cv.imread(path_in, cv.IMREAD_UNCHANGED)

    x1 = cfg_max2.X0
    y1 = cfg_max2.Y0
    x2: int = 0
    y2: int = 0

    if tag == 'image':
        x2 = int(cfg_max2.x_src)
        y2 = int(cfg_max2.y_src)

    if tag == 'templ':
        x2 = int(cfg_max2.x_dst)
        y2 = int(cfg_max2.y_dst)

    thickness = 2
    cv.line(magn,
            (x1, y1),
            (x2, y2),
            cfg_max2.dark_gray, thickness)

    path_out = cfg_max2.dir_debug + '/' + tag + '_result.png'
    cv.imwrite(path_out, magn)
