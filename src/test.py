import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1280,  720))
hammer_img = pygame.image.load("../img/hammer.png").convert_alpha()

hammer_idle = pygame.transform.scale(hammer_img,(500 ,500)) 

hammer_click = pygame.transform.rotate(hammer_idle,30)
background = pygame.image.load("../img/background.png").convert_alpha()
hammer = hammer_idle
pygame.mouse.set_visible(False)
while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            hammer = hammer_click
        if event.type == MOUSEBUTTONUP:
            hammer = hammer_idle
    
    screen.blit(hammer,(pygame.mouse.get_pos()[0]-80, pygame.mouse.get_pos()[1]-80))
    pygame.display.update()
    