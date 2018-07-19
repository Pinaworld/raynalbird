import pygame
from pygame.locals import *


pygame.init()

window = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("--FLAPPY RAYNAL--")


run = True


#RUNNER
while run:

        runHome = True
        runGame = True

        backHome = pygame.image.load("accBack.png").convert_alpha()
        window.blit(backHome, (0,0))
            
        pygame.display.flip()
        
        #HOME
        while runHome:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    runHome = False
                    run = False
                    runGame = False
                    
                    
            pygame.display.flip()


pygame.quit()

#GAME
