import main
import pygame
from pygame.locals import *

#hit_img = pygame.image.load('img/hit.png').convert_alpha()

class Player:
    def __init__(self):
        self.live = 3
        self.hitCount = 0
        self.missCount = 0
        self.combo = 0
        self.comboTime = 1
    def KnockEnemy(self, screen , x, y, hit: bool):
        pass

    def UpdateHitCount(self):
        self.hitCount += 1

    def UpdateMissCount(self):
        self.missCount += 1

    def UpdateScore(self, score: int):
        pass
        #self.score += score

    def UpdateLive(self, decsLive: int):
        self.live -= decsLive
        print("Live: " + str(self.live))

    def IsAlive(self):
        return False if self.live < 1 else True

    def getLives(self):
        return self.live
    def ClearCount(self):
        self.live = 3
        self.hitCount = 0
        self.missCount = 0
        self.combo = 0
        self.comboTime = 1
        
