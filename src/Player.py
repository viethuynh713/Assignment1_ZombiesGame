import pygame
from pygame.locals import *

class Player:
    def __init__(self, score: int = 0, combo: int = 0, comboTime: int = 0):
        self.score = score
        self.combo = combo
        self.comboTime = comboTime
        self.lives = 3
    def knockEnemy(self):
        pass
    def addScore(self):
        pass
    def subtractScore(self):
        pass
    def updateLives(self, n: int):
        print("updateLives")
    def getLives(self) -> int:
        return self.lives