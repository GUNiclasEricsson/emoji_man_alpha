import pygame
from settings import *


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        
        self.surface = pygame.image.load(EMOJI_SURFACE).convert()

        self.rect = self.surface.get_rect(topleft = FRUIT_1_START)

        