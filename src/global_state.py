# global constants

FPS_MAX = 60
CURRENT_FRAME = 0

# inputs

MOUSE_LMB_DOWN = False
MOUSE_LMB_UP = False
MOUSE_LMB_PRESSED = False
MOUSE_POS = (0,0)

# sprite groups (rendering + updating)

PARTICLE_GROUP = []
GUI_GROUP = []
ALL_GROUPS = PARTICLE_GROUP, GUI_GROUP # GUI renders last
