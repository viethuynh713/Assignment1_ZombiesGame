from enum import Enum

class EnemyState(Enum):
    GROWING = 0
    STANDING = 1
    DIVING = 2

class State(Enum):
    INIT = 0,
    PLAYING = 1,
    PAUSE = 2,
    END = 3,
    TUTORIAL = 4,