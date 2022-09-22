import pygame, sys
from pygame.locals import *
from pygame import mixer
import Enemy

class Bomb(Enemy.Enemy):
    def __init__(self, enemyManager, position: tuple, frame: int) -> None:
        super().__init__(enemyManager, position, frame)
    

    def hitHammer(self, player) -> None:
        if self.canGetHit:
            # Play sound
            hit_hammer_sound = mixer.Sound('../Sound/hit_enemy.mp3')
            hit_hammer_sound.play()
            # Add score
            player.UpdateLive(player.getLives())
            self.destroy()


    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255, 0, 0), (self.hitBox.left, self.hitBox.top, self.hitBox.width, self.hitBox.height))