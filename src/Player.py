import main
import pygame
from pygame.locals import *

#hit_img = pygame.image.load('img/hit.png').convert_alpha()

class Player:
    def __init__(self):
        self.score = 0
        self.live = 3
        self.hitCount = 0
        self.missCount = 0
        self.combo = 0
        self.comboTime = 1
    def KnockEnemy(self, screen , x, y, hit: bool):
        pass

    def UpdateHitCount(self):
        print("Hit enemy")
        self.hitCount += 1

    def UpdateMissCount(self):
        print("Hit bomb")
        self.hitCount += 1

    def UpdateScore(self, score: int):
        self.score += score

    def UpdateLive(self, decsLive: int):
        self.live -= decsLive

    def IsAlive(self):
        return False if self.live < 1 else True

    def getLives(self):
        return self.live
