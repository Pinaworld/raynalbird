import pygame
from pygame.locals import *

from classes import *
from const import *


pygame.init()

window = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("--FLAPPY RAYNAL--")


run = True


#RUNNER
while run:

        runHome = True
        runGame = False

        backHome = pygame.image.load("homeBack.png").convert_alpha()
        backGame = pygame.image.load("gameBack.png").convert_alpha()
            
        pygame.display.flip()
        
        #HOME
        while runHome:

            pygame.time.Clock().tick(30)
            window.blit(backHome, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    runHome = False
                    run = False
                    runGame = False
                    print("QuitOnHome")
                if event.type == KEYDOWN and event.key != K_ESCAPE:
                    print("RunningGame")
                    runGame = True
                    runHome = False
            pygame.display.flip()

            
        #GAME
        while runGame:
            window.blit(backGame, (0, 0))
            
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    runHome = True
                    runGame = False
                    print("GameToHome")
                    
            pygame.display.flip()


            
pygame.quit()

#GAME
