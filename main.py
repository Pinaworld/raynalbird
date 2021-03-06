import pygame
from pygame.locals import *

from classes import *
from const import *


pygame.init()

window = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("--FLAPPY RAYNAL--")


run = True

def birdMove(x, y, bird):
        window.blit(bird, (x,y))
        
def score(count):
        fonty = pygame.font.Font('BradBunR.ttf', 16)
        text = fonty.render("score : " + str(count), True, white)
        window.blit(text, [10,0])

def msgGameOver(picGameOver):

    fonty = pygame.font.Font('BradBunR.ttf',20)

    text = fonty.render("Press any button", True, (0,0,255))

    window.blit(text, [1280/2, 600/2])

    pygame.display.update()



        
#RUNNER
while run:

        runHome = True
        runGame = False

        backHome = pygame.image.load(pic_home).convert_alpha()
        backLevel = pygame.image.load(pic_level).convert_alpha()
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
                
            window.blit(backLevel, (0, 0))
            #LEVEL
            
            runGameEasy = False
            runGameMedium = False
            runGameHard = False

            y_move = 0

            alive = True #variable pour l'echec

            birdy = Bird("pics/upflap.png","pics/downflap.png")
            
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

                #EASY    
                while runGameEasy:
                                
                        for event in pygame.event.get():
                                window.blit(backGame, (0 ,0))
                                
                                birdy.y += 50
                                if event.type == QUIT:
                                        run = False
                                        runHome = False
                                        runGame = False
                                        runGameEasy = False
                                        print("ExitFromEasy")

                                if event.type == KEYDOWN and event.key == K_ESCAPE:
                                        runGameEasy = False
                                        runGame = True        
                                       
                                if event.type == KEYDOWN and event.key == K_SPACE:
                                        y_move = -5
                                if event.type == KEYUP:
                                        y_move = 5
                                        
                        birdy.y += y_move
                        birdMove(birdy.x, birdy.y, birdy.up)     
                        pygame.display.update()        
                pygame.display.flip()

                
                #MEDIUM    
                while runGameMedium:
                                
                        for event in pygame.event.get():
                                
                                window.blit(backGame, (0 ,0))
                                
                                if event.type == QUIT:
                                        run = False
                                        runHome = False
                                        runGame = False
                                        runGameMedium = False
                                        print("ExitFromEasy")

                                if event.type == KEYDOWN and event.key == K_ESCAPE:
                                        runGameMedium = False
                                        runGame = True        
                                       
                                if event.type == KEYDOWN and event.key == K_SPACE:
                                        msgGameOver(pic_gameover)
                                        
   
                        pygame.display.update()        
                pygame.display.flip()                
            pygame.display.flip()
        
        
            
pygame.quit()

