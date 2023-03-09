import pygame

class Emojiman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        emoji_walk_1 = pygame.image.load(' LÄGG IN BILD HÄR ').convert_alpha()
        emoji_walk_2 = pygame.image.load(' LÄGG IN BILD HÄR ').convert_alpha()
        self.player_walk = [emoji_walk_1,emoji_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(' LÄGG IN BILD HÄR ').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(bottomleft = (80, 295)) # Var ska han/hon/hen/den börja?
        self.gravity = 0
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= 300: # Detta värde fungerar inte, behöver importeras från annan kod - ground.rect istället för 300
            self.gravity = -20
        if keys [pygame.K_a]:
          #move left
        if keys [pygame.K_d]:
          #move right
            
    def apply_gravity(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: # Ground rect - se ovan
            self.rect.bottom = 300 # Ground_rect - se ovan
            
    def animation_state(self):
        if self.rect.bottom > 300:
            self.image = self.player_jump
            
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
                
            self.image = self.player_walk[int(self.player_index)]

            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
