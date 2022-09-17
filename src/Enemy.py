import math
import pygame
from pygame.locals import *
from constant import *
import EnemyManager
import Player

class Enemy:
    def __init__(self, enemyManager, position: tuple) -> None:
        # logic
        self.enemyManager = enemyManager
        self.scale = SCALE_A * position[1] + SCALE_B
        widthHitBox = ZOMBIE_WIDTH_HITBOX * self.scale
        heightHitBox = ZOMBIE_HEIGHT_HITBOX * self.scale
        self.hitBox = Rect(position[0] - widthHitBox / 2, position[1] - heightHitBox, widthHitBox, heightHitBox)
        self.canGetHit = False
        self.actionTime = 0
        # image
        self.spriteLst = []
        for i in range(0, ZOMBIE_SPRITE_LENGTH):
            self.spriteLst.append("../img/Zombie/up" + str(i + 1) + ".png")
        self.sprite = self.spriteLst[0]
        self.isUpping = True


    def act(self) -> None:
        self.actionTime += 1
        if self.canGetHit:
            if self.actionTime == ZOMBIE_STANDING_TIME:
                self.canGetHit = False
                self.actionTime = 0
        else:
            if self.actionTime == ZOMBIE_CHANGE_STATE_TIME:
                if self.isUpping:
                    self.isUpping = False
                    self.canGetHit = True
                    self.actionTime = 0
                else:
                    self.destroy()


    def hitHammer(self, player) -> None:
        if self.canGetHit:
            print("hitHammer")
            player.addScore()
            self.destroy()


    def isCollideHammer(self, position: tuple) -> bool:
        print(self.hitBox.topleft)
        if self.hitBox.collidepoint(position[0], position[1]):
            print("collideHammer")
            return True
        return False


    def getHitBox(self) -> Rect:
        return self.hitBox


    def draw(self, screen) -> None:
        self.loadSprite()
        sprite = pygame.image.load(self.sprite).convert_alpha()
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * self.scale, sprite.get_height() * self.scale))
        screen.blit(sprite, (self.hitBox.left, self.hitBox.top + (self.hitBox.height - sprite.get_height())))


    def loadSprite(self) -> None:
        if not self.canGetHit:
            idx = math.floor(self.actionTime / (ZOMBIE_CHANGE_STATE_TIME / ZOMBIE_SPRITE_LENGTH))
            if not self.isUpping:
                idx = ZOMBIE_SPRITE_LENGTH - idx - 1
                if idx < 0:
                    idx = 0
            self.sprite = self.spriteLst[idx]

    
    def destroy(self) -> None:
        self.enemyManager.removeEnemy(self)
        
class Zombie(Enemy):
    def __init__(self, enemyManager, position: tuple) -> None:
        Enemy.__init__(enemyManager, position)
class Boom(Enemy):
    def __init__(self, enemyManager, position: tuple) -> None:
        Enemy.__init__(enemyManager, position)