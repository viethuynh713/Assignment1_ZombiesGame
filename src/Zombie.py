import math
import pygame, sys
from pygame.locals import *
from constant import *
import enumType
import Enemy
import Player

class Zombie(Enemy.Enemy):
    def __init__(self, enemyManager, position: tuple, frame: int) -> None:
        super().__init__(enemyManager, position, frame)

    
    def hitHammer(self, player) -> None:
        if self.canGetHit:
            player.UpdateScore(10)
            self.destroy()

    
    def actAfterDive(self, player) -> None:
        player.UpdateLive(1)

    
    def draw(self, screen) -> None:
        # pygame.draw.rect(screen, (0, 0, 255), (self.hitBox.left, self.hitBox.top, self.hitBox.width, self.hitBox.height))
        self.loadSprite()
        sprite = pygame.image.load(self.sprite).convert_alpha()
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * self.scale, sprite.get_height() * self.scale))
        screen.blit(sprite, (self.hitBox.left, self.hitBox.top))
    


    def loadSprite(self) -> None:
        if self.state != enumType.EnemyState.STANDING:
            idx = math.floor(self.actionTime / (self.changeStateTime / ZOMBIE_SPRITE_LENGTH))
            if self.state == enumType.EnemyState.DIVING:
                idx = ZOMBIE_SPRITE_LENGTH - idx - 1
                if idx < 0:
                    idx = 0
            self.sprite = self.spriteLst[idx]