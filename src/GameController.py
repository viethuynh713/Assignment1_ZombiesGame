
import random
import webbrowser
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
        self.state = State.INIT
        self.listHoleHaveEnemy = []
        self.GenerateListHole()
        self.isOpenSetting = False
        self.isVolumeDisable = False
        self.isMusicDisable = False
        self.offset = (0,0)
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
        #self.screen.blit(self.background, (0, 0))
        if self.state == State.INIT:
            # TODO: Draw panel game
            self.screen.blit(self.mainMenuTemplate, (285, -30))

            if button.Button(530, 355, self.playButton, 1).draw(self.screen):
                self.isOpenSetting = False
                self.state = State.PLAYING

            if button.Button(530, 555, self.exitButtonMenu, 1).draw(self.screen):
                self.state = State.EXITPOPUP

            if button.Button(530, 455, self.tutorialButton, 1).draw(self.screen):
                self.state = State.TUTORIAL
            
            if button.Button(1207, 21, self.settingIcon, 1).draw(self.screen):
                if self.isOpenSetting:
                    self.isOpenSetting = False
                else:
                    self.isOpenSetting = True
            
            if self.isOpenSetting:
                if self.isVolumeDisable:
                    if button.Button(1207, 98, self.volumeDisableIcon, 1).draw(self.screen):
                        self.isVolumeDisable = False
                else:
                    if button.Button(1207, 98, self.volumeActiveIcon, 1).draw(self.screen):
                        self.isVolumeDisable = True

                if self.isMusicDisable:
                    if button.Button(1207, 175, self.musicDisableIcon, 1).draw(self.screen):
                        self.isMusicDisable = False
                else:
                    if button.Button(1207, 175, self.musicActiveIcon, 1).draw(self.screen):
                        self.isMusicDisable = True
                
            if button.Button(1200, 640, self.aboutUsButton, 0.5).draw(self.screen):
                webbrowser.open("www.facebook.com")
                # will change
        if self.state == State.TUTORIAL:
            if button.Button(30, 640, self.backButton, 0.5).draw(self.screen):
                self.state = State.INIT

        if self.state == State.PLAYING:



            # TODO: Need to implêmnt action phase
            #       Need to return State.END when user lost the game    


            if button.Button(1207, 21, self.settingIcon, 1).draw(self.screen):
                self.state = State.PAUSE
                  
        if self.state == State.PAUSE:
            self.screen.blit(self.settingTemplate, (375, 156))
            if button.Button(464, 248, self.resumeButton, 1).draw(self.screen):
                self.state = State.PLAYING
            if button.Button(464, 333, self.exitButtonSetting, 1).draw(self.screen):
                self.state = State.INIT
            
            if self.isVolumeDisable:
                if button.Button(532, 429, self.volumeDisableIcon, 1).draw(self.screen):
                    self.isVolumeDisable = False
            else:
                if button.Button(532, 429, self.volumeActiveIcon, 1).draw(self.screen):
                    self.isVolumeDisable = True

            if self.isMusicDisable:
                if button.Button(683, 429, self.musicDisableIcon, 1).draw(self.screen):
                        self.isMusicDisable = False
            else:
                if button.Button(683, 429, self.musicActiveIcon, 1).draw(self.screen):
                        self.isMusicDisable = True
            
        if self.state == State.END:
            self.endTemplate = pygame.transform.scale(self.settingTemplate, (int(self.settingTemplate.get_width() * 1.3), int(self.settingTemplate.get_height() * 1.3)))
            self.screen.blit(self.endTemplate, (300, 98))
            if button.Button(467, 517, self.homeButton, 1).draw(self.screen):
                self.state = State.INIT
                self.InitGame()
            
            if button.Button(725, 517, self.restartButton, 1 ).draw(self.screen):
                self.state = State.PLAYING
                self.InitGame()


        if self.state == State.EXITPOPUP:
            self.screen.blit(self.exitPopupTemplate, (375+self.offset[0], 156 + self.offset[1]))
            if button.Button(480 + self.offset[0], 340 + self.offset[1], self.yesButton, 1).draw(self.screen):
                while True:
                    x = random.randint(-500, 500)
                    y = random.randint(-250, 250)
                    if (math.pow(x - self.offset[0], 2) + math.pow(y - self.offset[1], 2)>200):
                        self.offset = (x,y)
                        break

            if button.Button(480 + self.offset[0], 425 + self.offset[1], self.noButton, 1).draw(self.screen):
                self.state = State.INIT
                self.offset = (0,0)

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
        pygame.display.set_caption("Hammer Kings")
        # Set icon for the game
        icon = pygame.image.load("../icon/icon_game.png")
        pygame.display.set_icon(icon)
        # Set icon for the game
        self.background = pygame.image.load("../img/background.png")
        #self.screen.blit(background, (0, 0))

        # # Set up UI
        # # Init Game Screen
        self.mainMenuTemplate = pygame.image.load("../img/mainMenu_template.png")
        self.playButton = pygame.image.load("../img/play_button.png")
        self.exitButtonMenu = pygame.image.load("../img/exit_button_menu.png")
        self.tutorialButton = pygame.image.load("../img/tutorial_button.png")
        self.settingIcon = pygame.image.load("../icon/icon_setting.png")
        self.volumeActiveIcon = pygame.image.load("../icon/icon_volume.png")
        self.volumeDisableIcon = pygame.image.load("../icon/icon_muteVolume.png")
        self.musicActiveIcon = pygame.image.load("../icon/icon_sound.png")
        self.musicDisableIcon = pygame.image.load("../icon/icon_muteSound.png")
        self.settingTemplate = pygame.image.load("../img/setting_template.png")
        self.resumeButton = pygame.image.load("../img/resume_button.png")
        self.exitButtonSetting = pygame.image.load("../img/exit_button_setting.png")
        self.backButton = pygame.image.load("../img/back_button.png")
        self.yesButton = pygame.image.load("../img/yes_button.png")
        self.noButton = pygame.image.load("../img/no_button.png")
        self.homeButton = pygame.image.load("../icon/icon_home.png")
        self.restartButton = pygame.image.load("../icon/icon_restart.png")
        self.aboutUsButton = pygame.image.load("../img/aboutUs_button.png")
        self.exitPopupTemplate = pygame.image.load("../img/exit_popup_template.png")

        
        hammer_img = pygame.image.load("../img/hammer.png").convert_alpha()
        
        hammer_idle = pygame.transform.scale(hammer_img,(120 ,120)) 
        
        hammer_click = pygame.transform.rotate(hammer_idle,30)
        
        hammer = hammer_idle
        
        pygame.mouse.set_visible(False)
        background = pygame.image.load("../img/background.png")
        while True:
            self.screen.blit(background, (0, 0))
            self.HandleEventUI()
            #self.screen.blit(hammer, (0, 0))
            self.screen.blit(hammer,(pygame.mouse.get_pos()[0] - 40,pygame.mouse.get_pos()[1]-89))
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
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
            pygame.display.update()

    def EndGame(self):
        self.state = State.END
        print(self.player.hitCount)
        print(self.player.missCount)
    def InitGame(self):
        self.player.ClearCount()
        self.listEnemy.ClearAllEnemy()

