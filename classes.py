import pygame
from pygame.locals import * 
from const import *


class Perso:
	    def __init__(self, up, down, level):
                
                    self.up = pygame.image.load(haut).convert_alpha()
                    self.down = pygame.image.load(bas).convert_alpha()

                    self.case_x = 0
                    self.case_y = 0
                    self.x = 0
                    self.y = 0
                    #Direction par défaut
                    self.direction = self.droite
                    #Niveau dans lequel le personnage se trouve 
                    self.niveau = niveau
