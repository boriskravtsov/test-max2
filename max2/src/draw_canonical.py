# Mar-08-2025
# draw_canonical.py

import cv2 as cv
from pathlib import Path

from max2.src import cfg_max2


def draw_canonical(image, templ):

    canon_image_name = 'canon_' + cfg_max2.image_name
    canon_templ_name = 'canon_' + cfg_max2.templ_name

    path_image_canon = str(Path.cwd() / cfg_max2.dir_debug / canon_image_name)
    path_templ_canon = str(Path.cwd() / cfg_max2.dir_debug / canon_templ_name)

    cv.imwrite(path_image_canon, image)
    cv.imwrite(path_templ_canon, templ)
