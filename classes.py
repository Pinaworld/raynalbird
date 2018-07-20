import pygame
from pygame.locals import * 
from const import *


class Bird:
	    def __init__(self, up, down):
                
                    self.up = pygame.image.load(up).convert_alpha()
                    self.down = pygame.image.load(down).convert_alpha()

                    self.x = 100
                    self.y = 300

                    self.fly = self.up

