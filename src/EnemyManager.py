import imp
from tkinter.messagebox import NO
import pygame 
from pygame.locals import *
import Enemy

class EnemyManager:
    def __init__(self) -> None:
        self.enemyList = []


    def initZombie(self, position: tuple) -> None:
        zombie = Enemy.Enemy(self, position)
        self.enemyList.append(zombie)


    def initBomb(self, position: tuple) -> None:
        pass


    def actAllEnemy(self, screen) -> None:
        for enemy in self.enemyList:
            enemy.act()
            enemy.draw(screen)


    def hitHammer(self, position: tuple):
        for enemy in self.enemyList:
            if enemy.isColliderHammer(position):
                return enemy
        return None


    def removeEnemy(self, enemy) -> None:
        self.enemyList.remove(enemy)


    def getEnemyList(self) -> list:
        return self.enemyList