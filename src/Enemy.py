import math
import pygame
from pygame.locals import *
from constant import *
from enumType import *
import EnemyManager
import Player

class Enemy:
    def __init__(self, enemyManager, position: tuple) -> None:
        # logic
        self.enemyManager = enemyManager
        self.scale = SCALE_A * position[1] + SCALE_B
        widthHitBox = ZOMBIE_WIDTH_HITBOX * self.scale
        self.maxHeightHitBox = ZOMBIE_HEIGHT_HITBOX * self.scale
        heightHitBox = 0
        self.hitBox = Rect(position[0] - widthHitBox / 2, position[1] - heightHitBox, widthHitBox, heightHitBox)
        self.canGetHit = True
        self.actionTime = 0
        # image
        self.spriteLst = []
        for i in range(0, ZOMBIE_SPRITE_LENGTH):
            self.spriteLst.append("../img/Zombie/up" + str(i + 1) + ".png")
        self.sprite = self.spriteLst[0]
        self.state = EnemyState.GROWING


    def act(self, player) -> None:
        self.actionTime += 1
        if self.state == EnemyState.GROWING:
            self.hitBox = Rect(self.hitBox.left, self.hitBox.top - self.maxHeightHitBox / ZOMBIE_CHANGE_STATE_TIME, self.hitBox.width, self.hitBox.height + self.maxHeightHitBox / ZOMBIE_CHANGE_STATE_TIME)
            if self.actionTime == ZOMBIE_CHANGE_STATE_TIME:
                self.state = EnemyState.STANDING
                self.actionTime = 0
        elif self.state == EnemyState.STANDING:
            if self.actionTime == ZOMBIE_STANDING_TIME:
                self.state = EnemyState.DIVING
                self.actionTime = 0
        else:
            self.hitBox = Rect(self.hitBox.left, self.hitBox.top + self.maxHeightHitBox / ZOMBIE_CHANGE_STATE_TIME, self.hitBox.width, self.hitBox.height - self.maxHeightHitBox / ZOMBIE_CHANGE_STATE_TIME)
            if self.actionTime == ZOMBIE_CHANGE_STATE_TIME:
                self.actAfterDive(player)
                self.destroy()


    def actAfterDive(self, player) -> None:
        pass


    def hitHammer(self, player) -> None:
        pass


    def isCollideHammer(self, position: tuple) -> bool:
        if self.hitBox.collidepoint(position[0], position[1]):
            return True
        return False


    def getHitBox(self) -> Rect:
        return self.hitBox


    def draw(self, screen) -> None:
        pass

    
    def destroy(self) -> None:
        self.enemyManager.removeEnemy(self)