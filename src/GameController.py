
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
from Bomb import *
from Zombie import *

class GameController:
    def __init__(self, player: Player, enemyManager: EnemyManager) -> None:
        self.timeSpawn = 100# DEFAULT_TIME_SPAWN
        self.minTimeSpawn = 100
        self.maxTimeSpawn = 1200
        self.player = player
        self.listEnemy = enemyManager
        self.state = State.PLAYING
        self.listHoleHaveEnemy = []
        self.GenerateListHole()
        self.Play()

    def GenerateListHole(self):
        self.listHole = []
        self.listHole.append((600, 700))
        self.listHole.append((500, 500))
        self.listHole.append((300, 500))
        self.listHole.append((68, 231))
        self.listHole.append((335, 245))
        self.listHole.append((543, 227))
        self.listHole.append((78, 454))
        self.listHole.append((147, 380))
        self.listHole.append((331, 374))
        self.listHole.append((195, 497))
        self.listHole.append((87, 603))
        self.listHole.append((505, 522))
        self.listHole.append((1188, 512))
        self.listHole.append((979, 631))
        self.listHole.append((850, 540))
        self.listHole.append((684, 671))


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
            if random.randint(0,100) < 50:
                self.listEnemy.initBomb(self.listHole[random.randint(0,self.listHole.__len__()-1)])
            else:
                self.listEnemy.initZombie(self.listHole[random.randint(0,self.listHole.__len__()-1)])
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

        
        hammer_img = pygame.image.load("../img/hammer.png").convert_alpha()
        
        hammer_idle = pygame.transform.scale(hammer_img,(120 ,120)) 
        
        hammer_click = pygame.transform.rotate(hammer_idle,30)
        
        hammer = hammer_idle
        
        #pygame.mouse.set_visible(False)
        background = pygame.image.load("../img/background.png")
        while True:
            self.screen.blit(background, (0, 0))
            #Sself.screen.blit(hammer, (0, 0))
            self.screen.blit(hammer,(pygame.mouse.get_pos()[0] - 50,pygame.mouse.get_pos()[1]-89))
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:# and self.state == State.PLAYING:
                    #print(pygame.mouse.get_pos())
                    hammer = hammer_click
                    if self.state == State.PLAYING:
                        enemy = self.listEnemy.hitHammer(pygame.mouse.get_pos())
                        if enemy:
                            # TODO: Check type of enemy, if type of enemy is Boom -> subtract heart else increase hit score
                            if type(enemy) == Bomb:
                                self.player.UpdateMissCount()
                                enemy.hitHammer(self.player)
                                    
                            if type(enemy) == Zombie:
                                self.player.UpdateHitCount()
                                enemy.hitHammer(self.player)
                                
                        else:
                            # TODO: Increase the player miss score
                            self.player.UpdateMissCount()
                        
                elif event.type == MOUSEBUTTONUP:
                    hammer = hammer_idle
            if not self.player.IsAlive() and self.state == State.PLAYING:
                self.EndGame()
            if self.state == State.PLAYING:
                self.SpawnEnemy()
            #self.HandleEventUI()
            pygame.display.update()

    def EndGame(self):
        self.state = State.END
        print("End Game")
        print(self.player.hitCount)
        print(self.player.missCount)
    def InitGame(self):
        self.player = Player()
        
        self.listEnemy = EnemyManager()

