import math
import pygame
from pygame.locals import *
from constant import *
from enumType import *
import EnemyManager
import Player

class Enemy:
    def __init__(self, enemyManager, position: tuple, frame: int) -> None:
        # logic
        self.enemyManager = enemyManager
        self.scale = ENEMY_SCALE_A * position[1] + ENEMY_SCALE_B
        widthHitBox = ENEMY_WIDTH_HITBOX * self.scale
        self.maxHeightHitBox = ENEMY_HEIGHT_HITBOX * self.scale
        heightHitBox = 0
        self.hitBox = Rect(position[0] - widthHitBox / 2, position[1] - heightHitBox, widthHitBox, heightHitBox)
        self.changeStateTime = ENEMY_CHANGE_STATE_TIME * (ENEMY_REDUCTION_APPEAR_RATE ** (math.floor(frame / ENEMY_REDUCTION_TIME)))
        self.standingTime = ENEMY_STANDING_TIME * (ENEMY_REDUCTION_APPEAR_RATE ** (math.floor(frame / ENEMY_REDUCTION_TIME)))
        self.dieTime = ENEMY_DIED_TIME
        self.canGetHit = True
        self.actionTime = 0
        self.state = EnemyState.GROWING


    def act(self, player) -> None:
        self.actionTime += 1
        if self.state == EnemyState.GROWING:
            self.hitBox = Rect(self.hitBox.left, self.hitBox.top - self.maxHeightHitBox / self.changeStateTime, self.hitBox.width, self.hitBox.height + self.maxHeightHitBox / self.changeStateTime)
            if self.actionTime == self.changeStateTime:
                self.state = EnemyState.STANDING
                self.actionTime = 0
        elif self.state == EnemyState.STANDING:
            if self.actionTime == self.standingTime:
                self.state = EnemyState.DIVING
                self.actionTime = 0
        elif self.state == EnemyState.DIVING:
            self.hitBox = Rect(self.hitBox.left, self.hitBox.top + self.maxHeightHitBox / self.changeStateTime, self.hitBox.width, self.hitBox.height - self.maxHeightHitBox / self.changeStateTime)
            if self.actionTime == self.changeStateTime:
                self.actAfterDive(player)
                self.destroy()
        else:
            if self.actionTime == self.dieTime:
                self.destroy()


    def actAfterDive(self, player) -> None:
        pass


    def hitHammer(self, gameController, player) -> None:
        print("Enemy")


    def isCollideHammer(self, position: tuple) -> bool:
        if self.hitBox.collidepoint(position[0], position[1]):
            return True
        return False


    def changeToDiedState(self) -> None:
        self.canGetHit = False
        self.state = EnemyState.DIED
        self.actionTime = 0


    def getHitBox(self) -> Rect:
        return self.hitBox


    def draw(self, screen) -> None:
        pass

    
    def destroy(self) -> None:
        self.enemyManager.removeEnemy(self)
        
# class Zombie(Enemy):
#     def __init__(self, enemyManager, position: tuple) -> None:
#         Enemy.__init__(enemyManager, position)
# class Bomb(Enemy):
#     def __init__(self, enemyManager, position: tuple) -> None:
#         Enemy.__init__(enemyManager, position)