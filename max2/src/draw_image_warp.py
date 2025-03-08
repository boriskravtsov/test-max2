# Mar-08-2025
# draw_image_warp.py

import cv2 as cv
from pathlib import Path

from max2.src import cfg_max2


def draw_image_warp():

    path_in = str(Path.cwd() / cfg_max2.dir_debug / 'image.png')
    image_in = cv.imread(path_in, cv.IMREAD_UNCHANGED)

    angle: float = cfg_max2.angle_result
    scale: float = cfg_max2.scale_result
    mat_rotate = cv.getRotationMatrix2D(cfg_max2.center, angle, scale)

    image_out = cv.warpAffine(image_in, mat_rotate, cfg_max2.dsize_roi)

    path_out = str(Path.cwd() / cfg_max2.dir_debug / 'image_warp.png')
    cv.imwrite(path_out, image_out)
