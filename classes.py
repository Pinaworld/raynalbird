import pygame
from pygame.locals import * 
from const import *


class Bird:
	    def __init__(self, up, down):
                
                    self.up = pygame.image.load(up).convert_alpha()
                    self.down = pygame.image.load(down).convert_alpha()

                    self.case_x = 0
                    self.case_y = 0
                    self.x = 0
                    self.y = 0

                    self.fly = self.up

