import pygame 
from pygame.locals import *

# Declare const variables
HEIGHT_SCREEN = 900
WIDTH_SCREEN = 600

# Set up game
pygame.init()
sreen = pygame.display.set_mode((HEIGHT_SCREEN, WIDTH_SCREEN))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()