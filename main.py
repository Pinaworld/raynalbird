import pygame
from pygame.locals import *


pygame.init()

window = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("--FLAPPY RAYNAL--")
backHome = pygame.image.load("accBack.png").convert_alpha()
window.blit(backHome, (0,0))

pygame.display.flip()


runHome = True
runGame = True

#Accueil
while runHome:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE or event:
                runHome = False

            
    pygame.display.flip()

pygame.quit()
