from EnemyManager import EnemyManager
from Player import Player
import pygame
from pygame.locals import *
from main import *
from enum import Enum
class State(Enum):
    INIT = 0,
    PLAYING = 1,
    PAUSE = 2,
    END = 3
class GameController:
    def __init__(self, player: Player, enemyManager: EnemyManager) -> None:
        self.player = player
        self.listEnemy = enemyManager
        self.state = State.INIT
        self.GenerateListHole()
        self.Play()
        
    def GenerateListHole(self):
        self.listHole = []
        self.listHole.append(pygame.math.Vector2(1,1))
    
    def Play(self):
        # Initialize 
        pygame.init()
        # Set Resolution
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        # Set name of the game
        pygame.display.set_caption("Zombies Game")
        # Set icon for the game
        icon = pygame.image.load("../icon/icon_game.png")
        pygame.display.set_icon(icon)
        # Set icon for the game
        background = pygame.image.load("../img/background.jpg")
        self.screen.blit(background,(0,0))
        
        button = pygame.Rect(0, 100, 200, 200)
        pygame.draw.rect(self.screen,(0,0,0), button)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            print("Button")
                            
                
            pygame.display.update()
        
                    
    def EndGame(self):
        pass
    def PauseGame(self):
        pass
