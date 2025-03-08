# Mar-08-2025
# sey_params.py

from max2.src import cfg_max2


def set_params(n_peaks: int, canonical_size: int, cutoff: float):

    cfg_max2.n_peaks = n_peaks
    cfg_max2.canonical_size = canonical_size
    cfg_max2.cutoff = cutoff

    cfg_max2.size_dft = 2048
    temp = int(cfg_max2.size_dft * cfg_max2.cutoff)
    if temp % 2:
        cfg_max2.size_roi = temp - 1
    else:
        cfg_max2.size_roi = temp

    cfg_max2.dsize_roi = (cfg_max2.size_roi, cfg_max2.size_roi)
    cfg_max2.size_roi_half = cfg_max2.size_roi // 2
    cfg_max2.X0 = cfg_max2.size_roi_half
    cfg_max2.Y0 = cfg_max2.size_roi_half
    cfg_max2.center = (cfg_max2.X0, cfg_max2.Y0)
