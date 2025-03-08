# Mar-08-2025
# draw_difference_map.py

import sys
import os
import cv2 as cv

from max2.src import cfg_max2


def draw_difference_map(difference_map):

    # Save Magnitude in file as grayscale.
    # ---------------------------------------------------------
    difference_map_gray_path = cfg_max2.dir_debug + '/' + '_difference_map_gray.png'
    result = cv.imwrite(difference_map_gray_path, difference_map)

    if result is False:
        print('ERROR: draw_difference_map()')
        sys.exit(1)
    # ---------------------------------------------------------

    # Convert difference_map to ColorMap.
    # ---------------------------------------------------------
    if os.path.exists(difference_map_gray_path):

        difference_map_gray = cv.imread(difference_map_gray_path, cv.IMREAD_GRAYSCALE)

        os.remove(difference_map_gray_path)

        difference_map_color = cv.applyColorMap(difference_map_gray, cv.COLORMAP_TURBO)
    else:
        print("ERROR in draw_difference_map(): The file does not exist")
        sys.exit(1)
    # ---------------------------------------------------------

    difference_map_color_path = cfg_max2.dir_debug + '/' + '_difference_map.png'
    cv.imwrite(difference_map_color_path, difference_map_color)
