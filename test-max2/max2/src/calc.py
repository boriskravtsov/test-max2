# Apr-05-2025
# calc.py

import cv2 as cv
import numpy as np
from numpy import ndarray

from max2.src import cfg
from max2.src.magnitude import get_magn_roi, get_magn_half
from max2.src.get_peaks import get_peaks
from max2.src.create_table import create_table
from max2.src.draw_magn import draw_magn
from max2.src.draw_peaks import draw_peaks
from max2.src.draw_result import draw_result
from max2.src.draw_image_warp import draw_image_warp
from max2.src.draw_difference_map import draw_difference_map
from max2.src.utils_list import save_list_of_peaks_txt


def calc(image: ndarray, templ: ndarray) -> float:

    image_flt = image.astype(np.float32)
    templ_flt = templ.astype(np.float32)

    image_magn_roi = get_magn_roi(image_flt)
    image_magn_half = get_magn_half(image_magn_roi)
    image_list_of_peaks = get_peaks(image_magn_half)
    image_table = create_table(image_list_of_peaks)
    n_image_peaks = len(image_list_of_peaks)

    if cfg.debug_mode:
        draw_magn('image', image_magn_roi)
        draw_peaks('image', image_list_of_peaks)
        save_list_of_peaks_txt('image_list_of_peaks', image_list_of_peaks)
        
    templ_magn_roi = get_magn_roi(templ_flt)
    templ_magn_half = get_magn_half(templ_magn_roi)
    templ_list_of_peaks = get_peaks(templ_magn_half)
    templ_table = create_table(templ_list_of_peaks)
    n_templ_peaks = len(templ_list_of_peaks)
    
    if cfg.debug_mode:
        draw_magn('templ', templ_magn_roi)
        draw_peaks('templ', templ_list_of_peaks)
        save_list_of_peaks_txt('templ_list_of_peaks', templ_list_of_peaks)

    distance_result = np.finfo(np.float32).max
    difference_map_current = np.zeros(cfg.dsize_roi, dtype=np.float32)
    difference_map_result = np.zeros(cfg.dsize_roi, dtype=np.float32)

    for j in range(1, n_image_peaks):

        index_src = j
        x_src = image_table[j, 0]
        y_src = image_table[j, 1]
        length_src = image_table[j, 2]
        angle_src = image_table[j, 3]

        for i in range(1, n_templ_peaks):

            index_dst = i
            x_dst = templ_table[i, 0]
            y_dst = templ_table[i, 1]
            length_dst = templ_table[i, 2]
            angle_dst = templ_table[i, 3]

            angle: float = float(angle_dst - angle_src)
            scale: float = float(length_dst / length_src)
            mat_rotate = cv.getRotationMatrix2D(cfg.center, angle, scale)

            image_magn_roi_warp \
                = cv.warpAffine(image_magn_roi,
                                mat_rotate,
                                cfg.dsize_roi,
                                borderMode=cv.BORDER_TRANSPARENT)

            if cfg.debug_mode:
                distance_current, difference_map_current \
                    = calc_cont_map(np.float32(image_magn_roi_warp),
                                    np.float32(templ_magn_roi))
            else:
                distance_current \
                    = calc_cont(np.float32(image_magn_roi_warp),
                                np.float32(templ_magn_roi))

            if distance_current < distance_result:
                distance_result = distance_current

                if cfg.debug_mode:
                    difference_map_result = difference_map_current.copy()

                    cfg.index_src = index_src
                    cfg.index_dst = index_dst
                    cfg.x_src = x_src
                    cfg.y_src = y_src
                    cfg.x_dst = x_dst
                    cfg.y_dst = y_dst
                    cfg.angle_result = angle
                    cfg.scale_result = scale

    if cfg.debug_mode:
        draw_result('image', image_list_of_peaks)
        draw_result('templ', templ_list_of_peaks)
        draw_image_warp()
        draw_difference_map(difference_map_result)

    return distance_result


def calc_cont_map(
        magnitude_1: np.float32,
        magnitude_2: np.float32) -> (float, np.float32):

    arr_zero = np.zeros(cfg.dsize_roi, dtype=np.float32)
    arr_1 = np.maximum(magnitude_1, arr_zero)
    arr_2 = np.maximum(magnitude_2, arr_zero)

    arr_min = np.minimum(arr_1, arr_2)
    arr_max = np.maximum(arr_1, arr_2)

    difference_map = np.subtract(arr_max, arr_min, where=arr_min > 0)
    nonzero_count = np.count_nonzero(difference_map)

    if nonzero_count == 0:
        distance = 0.0
    else:
        distance = np.sum(difference_map) / nonzero_count

    return distance, difference_map


def calc_cont(
        magnitude_1: np.float32,
        magnitude_2: np.float32) -> float:

    arr_zero = np.zeros(cfg.dsize_roi, dtype=np.float32)
    arr_1 = np.maximum(magnitude_1, arr_zero)
    arr_2 = np.maximum(magnitude_2, arr_zero)

    arr_min = np.minimum(arr_1, arr_2)
    arr_max = np.maximum(arr_1, arr_2)

    difference_map = np.subtract(arr_max, arr_min, where=arr_min > 0)
    nonzero_count = np.count_nonzero(difference_map)

    if nonzero_count == 0:
        distance = 0.0
    else:
        distance = np.sum(difference_map) / nonzero_count

    return distance
