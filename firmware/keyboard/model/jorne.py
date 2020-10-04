# fmt: off

from ..matrix import Matrix
import board
from .backlight import Backlight

Matrix.ROWS = (board.P0_20, board.P0_13, board.P0_24, board.P0_09)
Matrix.COLS = (board.P0_30, board.P0_31, board.P0_29, board.P0_02, board.P1_13, board.P0_03)
Matrix.ROW2COL = False

# ESC   1   2   3   4   5   6   7   8   9   0   -   =  BACKSPACE
# TAB   Q   W   E   R   T   Y   U   I   O   P   [   ]   |
# CAPS  A   S   D   F   G   H   J   K   L   ;   "      ENTER
#LSHIFT Z   X   C   V   B   N   M   ,   .   /         RSHIFT
# LCTRL LGUI LALT          SPACE         RALT MENU  L1 RCTRL
COORDS = (
    0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,  0, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,  0, 52,  0,
    53, 55, 54,  0,  0, 56,  0,  0, 57, 58, 59, 60,  0,  0
)

def battery_level():
    return 100
