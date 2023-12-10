from os.path import dirname

# screen
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900

# cell
CELL_SIZE = 16

# paths
ROOT_DIR = dirname(__file__)
RESOURCES = f'{ROOT_DIR}/res/'
MAPS = f'{RESOURCES}maps/'
TEXTURES = f'{RESOURCES}textures/'

# colors
BG = (30, 30, 30)

del dirname
