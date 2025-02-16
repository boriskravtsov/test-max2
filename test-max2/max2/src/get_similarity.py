# Feb-13-2025
# get_similarity.py

import sys
import cv2 as cv

from max2.src import cfg_max2
from max2.src.to_canonical import to_canonical
from max2.src.calc_similarity import calc_similarity
from max2.src.draw_canonical import draw_canonical


def get_similarity(path_image: str, path_templ: str) -> float:

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

    similarity = calc_similarity(image_canon, templ_canon)

    return similarity
