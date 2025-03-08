# Mar-08-2025
# cfg_max2.py

debug_mode: bool = False

dir_data: str = ''
dir_debug: str = ''

image_name: str = ''
templ_name: str = ''
path_image: str = ''
path_templ: str = ''

n_peaks: int = 0

canonical_size: int = 0

size_dft: int = 0
cutoff: float = 0.0
size_roi: int = 0
dsize_roi = (0, 0)
size_roi_half: int = 0
X0: int = 0
Y0: int = 0
center = (0, 0)

param_similarity: float = 0.01

index_src: int = -1
index_dst: int = -1
x_src: float = 0
y_src: float = 0
x_dst: float = 0
y_dst: float = 0
angle_result: float = 0
scale_result: float = 0

# 1 of 3
# ---------------------------------------------------------
# colormap = 'HOT'
colormap = 'HSV'
# colormap = 'JET'
# colormap = 'TURBO'
# ---------------------------------------------------------

# colors (BGR)
# -----------------------------------------
black = (0, 0, 0)
maraschino = (0, 38, 255)
clover = (0, 143, 0)
aqua = (255, 150, 0)
cayenne = (0, 17, 148)
blueberry = (255, 51, 4)
magenta = (255, 64, 255)
ocean = (147, 84, 0)
nickel = (146, 146, 146)
moss = (81, 144, 0)
lemon = (0, 251, 255)
gray = (128, 128, 128)
dark_gray = (96, 96, 96)
white = (255, 255, 255)
# -----------------------------------------
