import math
import pygame, sys
from pygame.locals import *
from pygame import mixer
from constant import *
from enumType import *
import Enemy
import Player

class Zombie(Enemy.Enemy):
    def __init__(self, enemyManager, position: tuple, frame: int) -> None:
        super().__init__(enemyManager, position, frame)
        # image
        self.upSpriteLst = []
        for i in range(0, ZOMBIE_UP_SPRITE_LENGTH):
            self.upSpriteLst.append("../img/Zombie/up" + str(i + 1) + ".png")
        self.dieSpriteLst = []
        for i in range(0, ZOMBIE_DIE_SPRITE_LENGTH):
            self.dieSpriteLst.append("../img/Zombie/die" + str(i + 1) + ".png")
        self.sprite = self.upSpriteLst[0]

    
    def hitHammer(self, player) -> None:
        if self.canGetHit:
            # Play sound
            hit_hammer_sound = mixer.Sound('../Sound/hit_enemy.mp3')
            hit_enemy_sound = mixer.Sound('../Sound/stun.mp3')
            hit_hammer_sound.play()
            hit_enemy_sound.play()
            # Add score
            player.UpdateScore(10)
            self.changeToDiedState()

    
    def actAfterDive(self, player) -> None:
        player.UpdateLive(1)

    
    def draw(self, screen) -> None:
        self.loadSprite()
        sprite = pygame.image.load(self.sprite).convert_alpha()
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * self.scale, sprite.get_height() * self.scale))
        left = self.hitBox.left
        if self.state == EnemyState.DIED:
            top = self.hitBox.top + (pygame.image.load(self.dieSpriteLst[0]).convert_alpha().get_height() * self.scale - sprite.get_height())
        else:
            top = self.hitBox.top
        screen.blit(sprite, (left, top))


    def loadSprite(self) -> None:
        if self.state == EnemyState.DIED:
            idx = math.floor(self.actionTime / (self.dieTime / ZOMBIE_DIE_SPRITE_LENGTH))
            if idx >= ZOMBIE_DIE_SPRITE_LENGTH:
                idx = ZOMBIE_DIE_SPRITE_LENGTH - 1
            self.sprite = self.dieSpriteLst[idx]
        elif self.state != EnemyState.STANDING:
            idx = math.floor(self.actionTime / (self.changeStateTime / ZOMBIE_UP_SPRITE_LENGTH))
            if self.state == EnemyState.DIVING:
                idx = ZOMBIE_UP_SPRITE_LENGTH - idx - 1
                if idx < 0:
                    idx = 0
            elif idx >= ZOMBIE_UP_SPRITE_LENGTH:
                idx = ZOMBIE_UP_SPRITE_LENGTH - 1
            self.sprite = self.upSpriteLst[idx]