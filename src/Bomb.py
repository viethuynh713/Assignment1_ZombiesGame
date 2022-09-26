import math
import pygame, sys
from pygame.locals import *
from pygame import mixer
from constant import *
from enumType import *
import Enemy

class Bomb(Enemy.Enemy):
    def __init__(self, enemyManager, position: tuple, frame: int) -> None:
        super().__init__(enemyManager, position, frame)
        # image
        self.rootSprite = pygame.image.load("../img/HL.png").convert_alpha()
        self.sprite = self.rootSprite
    

    def hitHammer(self, player, gameController) -> None:
        if self.canGetHit:
            # Play sound
            if not gameController.getVolumeDisable():
                hit_hammer_sound = mixer.Sound('../Sound/hit_enemy.mp3')
                hit_bomb_sound = mixer.Sound('../Sound/HLsound.mp3')
                hit_hammer_sound.play()
                hit_bomb_sound.play()
            # Add score
            player.UpdateLive(player.getLives())
            self.changeToDiedState()


    def draw(self, screen) -> None:
        if self.state == EnemyState.DIED:
            pygame.draw.rect(screen, (255, 0, 0), (self.hitBox.left, self.hitBox.top, self.hitBox.width, self.hitBox.height))
        else:
            self.loadSprite()
            sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width() * self.scale, self.sprite.get_height() * self.scale))
            left = self.hitBox.left
            top = self.hitBox.top
            screen.blit(sprite, (left, top))


    def loadSprite(self) -> None:
        if self.state != EnemyState.STANDING and self.state != EnemyState.DIED:
            idx = math.floor(self.actionTime / (self.changeStateTime / BOMB_SPRITE_LENGTH))
            percent = (idx + 1) / BOMB_SPRITE_LENGTH
            if self.state == EnemyState.DIVING:
                percent = 1 - percent
            self.sprite = pygame.transform.chop(self.rootSprite, (self.rootSprite.get_width(), self.rootSprite.get_height() * percent, 0, self.rootSprite.get_height() * (1 - percent)))