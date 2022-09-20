import sys
import pygame
import button
from pygame.locals import *
from constant import *
import GameController
import Player
import EnemyManager




if __name__ == '__main__':
    player = Player.Player()
    
    enemyManager = EnemyManager.EnemyManager()
    
    enemyManager.initBomb((400, 400))
    enemyManager.initZombie((600, 500))
    enemyManager.initBomb((800, 700))
    
    gameController = GameController.GameController(player, enemyManager) 
    
