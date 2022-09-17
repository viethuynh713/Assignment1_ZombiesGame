import imp
import pygame 
from pygame.locals import *
from Player import Player
import main
import Enemy

class EnemyManager:
    def __init__(self) -> None:
        self.enemyList = []
    def initZombie(self, position: tuple) -> None:
        zombie = Enemy(position)
        self.enemyList.append(zombie)
    def initBomb(self, position: tuple) -> None:
        pass
    def hitHammer(self, position: tuple) -> Enemy:
        for enemy in self.enemyList:
            if enemy.isColliderHammer(position):
                return enemy
        return None
    def removeEnemy(self, enemy: Enemy) -> None:
        self.enemyList.remove(enemy)
    def getEnemyList(self) -> list:
        return self.enemyList