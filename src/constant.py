### General
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
FPS = 60
VERSION = 1.0
### Game Controller
DEFAULT_TIME_SPAWN = 5000*FPS
### Zombie
ENEMY_WIDTH_HITBOX = 70
ENEMY_HEIGHT_HITBOX = 97
ZOMBIE_SPRITE_LENGTH = 7
ENEMY_CHANGE_STATE_TIME = 0.2 * FPS
ENEMY_STANDING_TIME = 0.7 * FPS
ENEMY_REDUCTION_APPEAR_RATE = 0.9
ENEMY_REDUCTION_TIME = 60 * FPS
SKY_LINE_Y = 200
ENEMY_MIN_SCALE = 0.25
ENEMY_MAX_SCALE = 1
# scale = a * (y) + b
ENEMY_SCALE_A = (ENEMY_MAX_SCALE - ENEMY_MIN_SCALE) / (HEIGHT_SCREEN - SKY_LINE_Y)
ENEMY_SCALE_B = ENEMY_MAX_SCALE - HEIGHT_SCREEN * ENEMY_SCALE_A
