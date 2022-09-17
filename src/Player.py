import main
import pygame
from pygame.locals import *

class Player:
    def __init__(self, score, combo, comboTime):
        self.score = score
        self.combo = combo
        self.comboTime = comboTime
    def knockEnemy(self):
        pass
    def addScore(self):
        pass
    def subtractScore(self):
        pass