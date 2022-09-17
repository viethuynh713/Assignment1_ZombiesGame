import pygame 
from pygame.locals import *

# Declare const variables
HEIGHT_SCREEN = 1280
WIDTH_SCREEN = 720

# Set up game
pygame.init()
screen = pygame.display.set_mode((HEIGHT_SCREEN, WIDTH_SCREEN))
pygame.display.set_caption('Zombies v1.0')

# load background for the game

imp = pygame.image.load("D:\\Zombies\\img\\background.png").convert()   # address cua Bao
# imp = pygame.image.load("../img/background.png").convert()              # address cua Khanh
screen.blit(imp, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()