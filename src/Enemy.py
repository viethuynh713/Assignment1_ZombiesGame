import imp


import pygame
from pygame.locals import *
import EnemyManager
import Player

class Enemy:
    def __init__(self, enemyManager: EnemyManager, position: tuple) -> None:
        self.enemyManager = enemyManager
        widthHitBox = 30
        heightHitBox = 50
        self.hitBox = Rect(position[0] - widthHitBox / 2, position[1] - heightHitBox, widthHitBox, heightHitBox)
    def hitHammer(self, player: Player) -> None:
        player.addScore()
        self.enemyManager.removeEnemy(self)
    def isCollideHammer(self, position: tuple) -> bool:
        if self.hitBox.collidepoint(position[0], position[1]):
            return True
        return False
    def getHitBox(self) -> Rect:
        return self.hitBox
