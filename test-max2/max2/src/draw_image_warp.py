# Apr-05-2025
# draw_image_warp.py

import cv2 as cv
from pathlib import Path

from max2.src import cfg


def draw_image_warp():

    path_in = str(Path.cwd() / cfg.dir_debug / 'image.png')
    image_in = cv.imread(path_in, cv.IMREAD_UNCHANGED)

    angle: float = cfg.angle_result
    scale: float = cfg.scale_result
    mat_rotate = cv.getRotationMatrix2D(cfg.center, angle, scale)

    image_out = cv.warpAffine(image_in, mat_rotate, cfg.dsize_roi)

    path_out = str(Path.cwd() / cfg.dir_debug / 'image_warp.png')
    cv.imwrite(path_out, image_out)
