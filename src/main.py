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
    
    gameController = GameController.GameController(player, enemyManager) 
    
