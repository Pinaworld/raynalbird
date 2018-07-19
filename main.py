import pygame
from pygame.locals import *


pygame.init()

fen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("--FLAPPY RAYNAL--")
accueilBack = pygame.image.load("accBack.png").convert_alpha()
fen.blit(accueilBack, (0,0))

pygame.display.flip()
cont = True

while cont:
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                cont = False

            
    pygame.display.flip()

pygame.quit()
