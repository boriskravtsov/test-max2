# Apr-05-2025
# get_shapes_distance.py

import sys
import cv2 as cv

from max2.src import cfg
from max2.src.to_canonical import to_canonical
from max2.src.calc import calc
from max2.src.draw_canonical import draw_canonical


def get_shapes_distance(path_image: str, path_templ: str) -> float:

    """
    Call set_params(...) only when you need to
    change the default settings in cfg.py
    """
    # set_params(15, 100, 2048, 0.333)

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

    if cfg.debug_mode:
        draw_canonical(image_canon, templ_canon)

    distance = calc(image_canon, templ_canon)

    return distance


def set_params(n_peaks: int, canonical_size: int, size_dft: int, cutoff: float):

    cfg.n_peaks = n_peaks
    cfg.canonical_size = canonical_size
    cfg.size_dft = size_dft
    cfg.cutoff = cutoff

    temp = int(cfg.size_dft * cfg.cutoff)
    if temp % 2:
        cfg.size_roi = temp - 1
    else:
        cfg.size_roi = temp

    cfg.dsize_roi = (cfg.size_roi, cfg.size_roi)
    cfg.size_roi_half = cfg.size_roi // 2
    cfg.X0 = cfg.size_roi_half
    cfg.Y0 = cfg.size_roi_half
    cfg.center = (cfg.X0, cfg.Y0)
