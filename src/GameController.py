import random
from EnemyManager import EnemyManager
from Player import Player
import pygame
from pygame.locals import *
from button import Button
from main import *
from enum import Enum


FPS = 60
DEFAULT_TIME_SPAWN = 5000*FPS


class State(Enum):
    INIT = 0,
    PLAYING = 1,
    PAUSE = 2,
    END = 3,
    TUTORIAL = 4,


class GameController:
    def __init__(self, player: Player, enemyManager: EnemyManager) -> None:
        self.timeSpawn = DEFAULT_TIME_SPAWN
        self.minTimeSpawn = 1000
        self.maxTimeSpawn = 5000
        self.player = player
        self.listEnemy = enemyManager
        self.state = State.INIT
        self.GenerateListHole()
        self.Play()

    def GenerateListHole(self):
        self.listHole = []
        self.listHole.append(pygame.math.Vector2(1, 1))

    def HandleEventUI(self):
        if self.state == State.INIT:
            if self.play_button.draw(self.screen):
                State = State.PLAYING

            if self.exit_button.draw(self.screen):
                pygame.quit()

            if self.tutorial_button.draw(self.screen):
                State = State.TUTORIAL
                # TODO: implement tutorial mode

            if self.setting_button.draw(self.screen):
                self.isOpenSetting = True
        if self.tate == State.TUTORIAL:
            pass
        if self.state == State.PLAYING:
            pass
        if self.state == State.PAUSED:
            pass
        if self.state == State.END:
            pass

    def SpawnEnemy(self):
        if self.timeSpawn <= 0:
            if random.randint(0,100) < 10:
                self.listEnemy.initBomb()
            else:
                self.listEnemy.initZombie()
            self.timeSpawn = random.randint(self.minTimeSpawn, self.maxTimeSpawn)
            
        self.timeSpawn -= self.clock.tick(FPS)
        
        # TODO: draw enemy in list enemy
    
    def Play(self):
        # Initialize
        pygame.init()
        self.clock = pygame.time.Clock()
        # Set Resolution
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        # Set name of the game
        pygame.display.set_caption("Zombies Game")
        # Set icon for the game
        icon = pygame.image.load("../icon/icon_game.png")
        pygame.display.set_icon(icon)
        # Set icon for the game
        background = pygame.image.load("../img/background.jpg")
        self.screen.blit(background, (0, 0))

        # Set up UI
        self.play_button = Button()
        self.exit_button = Button()
        self.setting_button = Button()
        self.tutorial_button = Button()
        self.isOpenSetting = False

        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and self.state == State.PLAYING:
                    self.player.knockEnemy()
                    enemy = self.listEnemy.hitHammer(pygame.mouse.get_pos())
                    if enemy:
                        pass
                        # TODO: Check type of enemy, if type of enemy is Boom -> subtract heart else increase hit score
                    else:
                        # TODO: Increase the player miss score
                        pass
            self.SpawnEnemy()
            self.HandleEventUI()
            pygame.display.update()

    def EndGame(self):
        pass

    def PauseGame(self):
        pass
