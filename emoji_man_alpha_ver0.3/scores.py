import pygame
import random
from settings import *

class Watermelon(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Watermelon, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_watermelon1.png").convert_alpha()

        self.rect = self.surface.get_rect(center = (1520, 560))

        watermelon = self.rect

        


        
        
    def get_score(self, player):

        if pygame.Rect.colliderect(self.rect, player.rect):
            print("WATERMELON SCORE!")
            self.kill()

class Apples(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Apples, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_apple1.png").convert_alpha()

        self.rect = self.surface.get_rect(center = (1440, 1000))

        apple = self.rect

        


        
        
    def get_score(self, player):

        if pygame.Rect.colliderect(self.rect, player.rect):
            print("APPLE SCORE!")
            self.kill()
        
class Scores():
    def __init__(self, fruit_group):

        self.fruit_group = fruit_group

        self.current_score = 0

    def get_scores(self, player):
        for fruit in self.fruit_group:
            if pygame.Rect.colliderect(player.rect, fruit.rect):
                print("YOU SCOREED!")
                self.current_score += 1
                fruit.kill()
                #time = pygame.time.get_ticks()
                #print(time)


#clock = pygame.time.Clock()



class Score():
    def __init__(self):
        #score_surf = score_font.render('EmojiMan', False, (64, 64, 64))
        #self.start_time = 0
        #self.current_time = 0

        #self.score_amount = 0
        self.score_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 50)
        self.instruct_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 30)

        self.surface = pygame.image.load("assets/start_screen.png").convert_alpha()
        self.rect = self.surface.get_rect(x = 0, y = 0)

    

    def display_score(self, current_score):
        #self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time

        self.current_score = current_score
        
        self.score_surf = self.score_font.render(f'Score: {self.current_score}', False, (64,64,64))
        #self.score_rect = self.score_surf.get_rect (center = (400,50))
        SCREEN.blit(self.score_surf, (800, 70)) #, self.score_rect)

        #return self.current_time
    
    def score_reset(self): #, #current_score)
        #self.current_score = current_score
        return 0


    def game_over(self, current_score):
        SCREEN.blit(BACKGROUND, (0, 0))

        self.instruct_surf = self.instruct_font.render('Press ENTER to start the game', False, (64, 64, 64))
        self.instruct_rect = self.instruct_surf.get_rect(center = (960, 540))
        self.name_surf = self.score_font.render('EmojiMan in rect land', False, (64, 64, 64))
        self.name_rect = self.name_surf.get_rect(center = (960, 220))
        self.final_score = current_score
        SCREEN.blit(self.name_surf, self.name_rect)
        
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect,10)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect,10)

        self.score_message = self.score_font.render(f'Your score: {self.final_score}', False, (64, 64, 64))
        self.score_message_rect = self.score_message.get_rect(center = (960, 540))

        SCREEN.blit(self.surface, self.rect)

        if current_score == 2:
            SCREEN.blit(self.instruct_surf, self.instruct_rect)

        else:
            SCREEN.blit(self.score_message, self.score_message_rect)
            
    def update(self, current_score):
        self.display_score(current_score)


    

        


        

