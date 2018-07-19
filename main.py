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

        backHome = pygame.image.load(pic_home).convert_alpha()
        backGame = pygame.image.load(pic_game).convert_alpha()
            
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
                    print("Quit_On_Home")
                if event.type == KEYDOWN and event.key != K_ESCAPE:
                    print("Running_Game")
                    runGame = True
                    runHome = False
            pygame.display.flip()

            
        #GAME
        while runGame:
            window.blit(backGame, (0, 0))
            runGameEasy = False
            runGameMedium = False
            runGameHard = False

            alive = True
            
            for event in pygame.event.get():
                
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    runHome = True
                    runGame = False
                    print("Game_To_Home")
                    
                if event.type == QUIT:
                    run = False
                    runHome = False
                    runGame = False
                    print("Quit_On_Game")
                    
                if event.type == KEYDOWN and event.key == K_F1:
                    runGameEasy = True
                    runGameMedium = False
                    runGameHard = False

                    if alive == False:
                        runGameEasy = False
                        
                    print("Easy_Mode")
                    
                if event.type == KEYDOWN and event.key ==  K_F2:
                    runGameEasy = False
                    runGameMedium= True
                    runGameHard = False

                    if alive == False:
                        runGameMedium = False
                        
                    print("Medium_Mode")
                    
                if event.type == KEYDOWN and event.key ==  K_F3:
                    runGameEasy = False
                    runGameMedium= False
                    runGameHard = True
                    
                    if alive == False:
                        runGameHard = False
                        
                    print("Hard_Mode")
                pygame.display.flip()    
            pygame.display.flip()
        
        
            
pygame.quit()

