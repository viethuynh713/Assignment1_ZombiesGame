import pygame, sys
from pygame.locals import *
import Enemy

class Bomb(Enemy.Enemy):
    def __init__(self, enemyManager, position: tuple) -> None:
        super().__init__(enemyManager, position)
    

    def hitHammer(self, player) -> None:
        if self.canGetHit:
            player.updateLives(-player.getLives())
            self.destroy()


    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255, 0, 0), (self.hitBox.left, self.hitBox.top, self.hitBox.width, self.hitBox.height))