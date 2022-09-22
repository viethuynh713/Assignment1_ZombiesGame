import random
from EnemyManager import EnemyManager
from Player import *
import pygame
from pygame.locals import *
from button import Button
from main import *
from enum import Enum
from constant import *
import webbrowser

class State(Enum):
    INIT = 0,
    PLAYING = 1,
    PAUSE = 2,
    END = 3,
    TUTORIAL = 4,
    EXITPOPUP = 5


class GameController:
    def __init__(self, player: Player, enemyManager: EnemyManager) -> None:
        self.timeSpawn = DEFAULT_TIME_SPAWN
        self.minTimeSpawn = 1000
        self.maxTimeSpawn = 5000
        self.player = player
        self.listEnemy = enemyManager
        self.state = State.INIT
        self.listEnemyPosition = []
        self.GenerateListHole()
        self.isOpenSetting = False
        self.isVolumeDisable = False
        self.isMusicDisable = False
        self.Play()


    def GenerateListHole(self):
        self.listHole = []
        self.listHole.append((600, 700))
        self.listHole.append((500, 500))

    def HandleEventUI(self):
        self.screen.blit(self.background, (0, 0))
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
                
            if button.Button(30, 640, self.aboutUsButton, 0.5).draw(self.screen):
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
            
            if button.Button(725, 517, self.restartButton, 1 ).draw(self.screen):
                self.state = State.PLAYING


        if self.state == State.EXITPOPUP:
            self.screen.blit(self.settingTemplate, (375, 156))
            if button.Button(480, 340, self.yesButton, 1).draw(self.screen):
                pygame.quit()
                sys.exit()
            
            if button.Button(480, 425, self.noButton, 1).draw(self.screen):
                self.state = State.INIT

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

        while True:
            self.clock.tick(FPS)
            
            self.HandleEventUI()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and self.state == State.PLAYING:
                    # self.player.knockEnemy()
                    # enemy = self.listEnemy.hitHammer(pygame.mouse.get_pos())
                    # if enemy:
                    #     pass
                    #     # TODO: Check type of enemy, if type of enemy is Boom -> subtract heart else increase hit score
                    # else:
                    #     # TODO: Increase the player miss score
                    pass
            #self.SpawnEnemy()
            #print (self.state)
            pygame.display.update()

    def EndGame(self):
        pass

    def PauseGame(self):
        pass
