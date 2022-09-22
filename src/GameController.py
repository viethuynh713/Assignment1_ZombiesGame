import random
from EnemyManager import EnemyManager
from Player import *
import pygame
from pygame.locals import *
from button import Button
from main import *
from enum import Enum
from constant import *
from enumType import *

class GameController:
    def __init__(self, player: Player, enemyManager: EnemyManager) -> None:
        self.timeSpawn = DEFAULT_TIME_SPAWN
        self.minTimeSpawn = 1000
        self.maxTimeSpawn = 5000
        self.player = player
        self.listEnemy = enemyManager
        self.state = State.PLAYING
        self.listEnemyPosition = []
        self.GenerateListHole()
        self.Play()

    def GenerateListHole(self):
        self.listHole = []
        self.listHole.append((600, 700))
        self.listHole.append((500, 500))

    def HandleEventUI(self):
        if self.state == State.INIT:
            # TODO: Draw panel game
            if self.play_button.draw(self.screen):
                self.isOpenSetting = False
                State = State.PLAYING

            if self.exit_button.draw(self.screen):
                pygame.quit()

            if self.tutorial_button.draw(self.screen):
                State = State.TUTORIAL
            if self.setting_button.draw(self.screen):
                self.isOpenSetting = True
            if self.isOpenSetting:
                if self.musicMenu_button.draw(self.screen):
                    # TODO: current state = ! current state && change icon
                    pass
                if self.soundMenu_button.draw(self.screen):
                    # TODO: Same 
                    pass
        if self.state == State.TUTORIAL:
            
            # TODO: implement tutorial mode
            pass
        if self.state == State.PLAYING:
            # TODO: draw list heart images
            if self.setting_button.draw(self.screen):
                self.state = State.PAUSE
                  
        if self.state == State.PAUSED:
            # TODO: draw template setting
            if self.resume_button.draw(self.screen):
                state = State.PLAYING
            if self.exitSetting_button.draw(self.screen):
                # TODO: clear hit count, miss count,list enemy
                
                state = State.INIT
            
        if self.state == State.END:
            pass

    def SpawnEnemy(self):
        if self.timeSpawn <= 0:
            if random.randint(0,100) < 10:
                self.listEnemy.initBomb(self.listHole[random.randint(0,self.listHole.size)])
            else:
                self.listEnemy.initZombie(self.listHole[random.randint(0,self.listHole.size)])
            self.timeSpawn = random.randint(self.minTimeSpawn, self.maxTimeSpawn)
            
        self.timeSpawn -= self.clock.tick(FPS)
        
        # TODO: draw enemy in list enemy
        self.listEnemy.actAllEnemy(self.screen,self.player)
    
    def Play(self):
        # Initialize
        pygame.init()
        self.clock = pygame.time.Clock()
        # Set Resolution
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        # Set name of the game
        pygame.display.set_caption("Hammer King")
        # Set icon for the game
        icon = pygame.image.load("../icon/icon_game.png")
        pygame.display.set_icon(icon)
        # Set icon for the game
        background = pygame.image.load("../img/background.png")
        self.screen.blit(background, (0, 0))

        # # Set up UI
        # # Init Game Screen
        # self.play_button = Button()
        # self.exitMenu_button = Button()
        # self.setting_button = Button()
        # self.tutorial_button = Button()
        # self.soundMenu_button = Button()
        # self.musicMenu_button = Button()
        # # Settings panel 
        # self.soundSetting_button = Button()
        # self.musicSetting_button = Button()
        # self.resume_button = Button()
        # self.exitSetting_button = Button()
        
        # # End game panel
        # self.home_button = Button()
        # self.restart_button = Button()
        # TODO : Text of hit count and miss count of game.
        # TODO : Init list heart image
        self.isOpenSetting = False

        self.listEnemy.initBomb((400, 400))
        # self.listEnemy.initZombie((600, 500))
        self.listEnemy.initBomb((800, 700))

        while True:
            self.clock.tick(FPS)
            self.screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and self.state == State.PLAYING:
                    # self.player.KnockEnemy()
                    enemy = self.listEnemy.hitHammer(pygame.mouse.get_pos())
                    if enemy:
                        enemy.hitHammer(self.player)
                        # TODO: Check type of enemy, if type of enemy is Boom -> subtract heart else increase hit score
                    else:
                        # TODO: Increase the player miss score
                        pass
            self.SpawnEnemy()
            #self.HandleEventUI()
            print(self.player.getLives())
            pygame.display.update()

    def EndGame(self):
        pass

    def PauseGame(self):
        pass
