import pygame
from settings import *


class EmojiMan(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(EmojiMan, self).__init__()
        
        self.surface = pygame.image.load(EMOJI_SURFACE).convert()

        self.rect = self.surface.get_rect(topleft = PLAYER_START)

        self.bottom = self.rect.bottom

        self.mask = pygame.mask.Mask((self.rect.width, self.rect.height), True)
        #print(self.mask)


        self.direction = pygame.math.Vector2()
        self.steps = 4
        self.jump_speed = 5
        self.gravity = 0.2
        self.jumped = False
        self.power_up = False


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        #print(self.rect.bottom)#self.direction, self.rect.y)

        #if self.rect.bottom > 840:
        #    self.rect.bottom = 840
        #    self.direction.y = 0
            #print("BOTTOM")
        





    def update(self, key):
        if key[UP]:
            self.direction.y = -self.steps
        #else: 
        #    self.direction.y = 0
        #if key[DOWN]:
        #    self.direction.y = self.steps
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
        if key[SPACE] and self.jumped == False:
            self.direction.y = -self.jump_speed
            self.jumped = True

    def collision(self, player, collision_sprites):        
        for sprite in collision_sprites:
            if sprite.rect.colliderect(player.rect):
                #print(sprite.rect, "COLLISION")
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

        self.apply_gravity()


        for sprite in collision_sprites:
            if sprite.rect.colliderect(player.rect):                
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                    #self.direction.y = 0
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.jumped = False




            #collision = pygame.Rect.colliderect(player.rect, sprite.rect.top):
            #if collision:

                    

        
        
        
        
        
        
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


