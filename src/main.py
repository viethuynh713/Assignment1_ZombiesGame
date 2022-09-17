import sys
import pygame
from GameController import GameController 
import button
from pygame.locals import *
from constant import *
import GameController
import Player
import EnemyManager

# Set up game
pygame.init()
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption('Zombies v' + str(VERSION))

#game variable
game_paused = False
menu_state = "main"
#font 

font = pygame.font.SysFont("Arialblack", 40)

#
TEXT_COL = (255,255,255)

# load background for the game
background = pygame.image.load('../img/background.png').convert_alpha()
play_icon = pygame.image.load('../icon/Play.png').convert_alpha()

# button in menu
play_button = button.Button(WIDTH_SCREEN/2 - 50, HEIGHT_SCREEN/2 - 50, play_icon, 0.1)


def drawBackGround():
    screen.blit(background, (0,0))

#drawBackGround()

run = True

gameController = GameController.GameController()
player = Player.Player()
enemyManager = EnemyManager.EnemyManager()
enemyManager.initBomb((400, 400))
enemyManager.initZombie((600, 500))
enemyManager.initBomb((800, 700))

FPSCLOCK = pygame.time.Clock()

while run:
    screen.fill((52,78,91))
    drawBackGround()
    if game_paused == True:
        if menu_state == "main":
            if play_button.draw(screen):
                game_paused = False
    else:
        # enemy = enemyManager.hitHammer((600, 450))
        # if enemy != None:
        #     enemy.hitHammer(player)
        enemyManager.actAllEnemy(screen, player)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FPSCLOCK.tick(FPS)