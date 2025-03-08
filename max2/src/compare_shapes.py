# Mar-08-2025
# compare_shapes.py

import sys
import cv2 as cv

from max2.src import cfg_max2
from max2.src.to_canonical import to_canonical
from max2.src.calc import calc
from max2.src.draw_canonical import draw_canonical


def compare_shapes(path_image: str, path_templ: str) -> (float, float):

    image_gray = cv.imread(path_image, cv.IMREAD_GRAYSCALE)
    if image_gray is None:
        print(f'\nERROR: Unable to read {path_image}.')
        sys.exit(1)

    templ_gray = cv.imread(path_templ, cv.IMREAD_GRAYSCALE)
    if templ_gray is None:
        print(f'\nERROR: Unable to read {path_templ}.')
        sys.exit(1)

    image_canon = to_canonical(image_gray)
    templ_canon = to_canonical(templ_gray)

    if cfg_max2.debug_mode:
        draw_canonical(image_canon, templ_canon)

    distance, similarity = calc(image_canon, templ_canon)

    return distance, similarity
