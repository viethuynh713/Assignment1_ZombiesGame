import main
import pygame
from pygame.locals import *

hit_img = pygame.image.load('img/hit.png').convert_alpha()

class Player:
    def __init__(self) -> None:
        pass
    # def __init__(self, score: int, live: int, hitCount: int, missCount: int, combo:int, timeCombo: int) -> None:
    #     self.score = score
    #     self.live = live
    #     self.hitCount = hitCount
    #     self.missCount = missCount
    #     self.combo = combo
    #     self.comboTime = timeCombo
    def KnockEnemy(self, screen , x, y, hit: bool):
        pass

    def UpdateHitCount(self):
        self.hitCount += 1

    def UpdateMissCount(self):
        self.hitCount += 1

    def UpdateScore(self, score: int):
        self.score += score

    def UpdateLive(self, decsLive: int):
        self.live -= decsLive

    def IsAlive(self):
        return False if self.live < 1 else True

    def getLives(self):
        return self.live