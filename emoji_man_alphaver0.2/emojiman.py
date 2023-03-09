import pygame
from settings import *


class EmojiMan(pygame.sprite.Sprite):
    def __init__(self):
        super(EmojiMan, self).__init__()
        
        self.surface = pygame.image.load(EMOJI_SURFACE).convert()

        self.rect = self.surface.get_rect(topleft = PLAYER_START)

        self.bottom = self.rect.bottom

        self.mask = pygame.mask.Mask((self.rect.width, self.rect.height), True)
        #print(self.mask)


        self.direction = pygame.math.Vector2()
        self.steps = 4
        self.jump_speed = 10
        self.gravity = 0.2


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        print(self.rect.bottom)#self.direction, self.rect.y)

        if self.rect.bottom > 800:
            self.direction.y = 0
            print("BOTTOM")
        





    def update(self, key):
        if key[UP]:
            self.direction.y = -self.steps
        #else: 
        #    self.direction.y = 0
        if key[DOWN]:
            self.direction.y = self.steps
        #else: 
        #    self.direction.y = 0
        if key[LEFT]:
            self.direction.x = -self.steps
            self.rect.x += self.direction.x
        #else: 
        #    self.direction.x = 0
        if key[RIGHT]:
            self.direction.x = self.steps
            self.rect.x += self.direction.x
        #else: 
        #    self.direction.x = 0
        if key[SPACE]:
            self.direction.y = -self.jump_speed

       

        
        
        
        
        
        
        #if key[UP]:
        #    self.rect.move_ip(0, -self.steps)
        #if key[DOWN]:
        #    self.rect.move_ip(0, self.steps)
        #if key[LEFT]:
        #    self.rect.move_ip(-self.steps, 0)
        #if key[RIGHT]:
        #    self.rect.move_ip(self.steps, 0)
        #if key[SPACE]:
        #    self.rect.move_ip(0, -self.steps * self.jump_speed)


