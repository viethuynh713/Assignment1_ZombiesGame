import pygame 
from pygame.locals import *
from pygame import mixer
import Zombie
import Bomb

class EnemyManager:
    def __init__(self) -> None:
            self.enemyList = []


    def initZombie(self, position: tuple) -> None:
        zombie = Zombie.Zombie(self, position,1)
        self.enemyList.append(zombie)


    def initBomb(self, position: tuple) -> None:
        bomb = Bomb.Bomb(self, position,1)
        self.enemyList.append(bomb)


    def actAllEnemy(self, screen, player) -> None:
        for enemy in self.enemyList:
            enemy.act(player)
            enemy.draw(screen)


    def hitHammer(self, position: tuple):
        for enemy in self.enemyList:
            if enemy.isCollideHammer(position):
                return enemy
        miss_enemy_sound = mixer.Sound('../Sound/miss_enemy.mp3')
        miss_enemy_sound.play()
        return None


    def removeEnemy(self, enemy) -> None:
        self.enemyList.remove(enemy)


    def getEnemyList(self) -> list:
        return self.enemyList