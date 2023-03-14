import pygame

clock = pygame.time.Clock()

WH = (1920, 1080)

SCREEN = pygame.display.set_mode(WH)

class Score():
    def __init__(self, start_time = 0, current_time = 0):
        #score_surf = score_font.render('First', False, (64, 64, 64))
        self.start_time = start_time
        self.current_time = current_time
        self.score_font = pygame.font.Font('fonts/RETRO_SPACE.ttf', 50)
        self.instruct_font = pygame.font.Font('fonts/RETRO_SPACE.ttf', 30)

    

    def display_score(self):
        self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        
        self.score_surf = self.score_font.render(f'Score: {self.current_time}', False, (64,64,64))
        self.score_rect = self.score_surf.get_rect (center = (400,50))
        SCREEN.blit(self.score_surf, self.score_rect)

        return self.current_time
    
    def score_reset(self):
        self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        


    def game_over(self):

        SCREEN.fill((94, 129, 162))
        self.instruct_surf = self.instruct_font.render('Press ESC to start the game', False, (138, 25, 64))
        self.instruct_rect = self.instruct_surf.get_rect(center = (400, 300))
        self.name_surf = self.score_font.render('First', False, (64, 64, 64))
        self.name_rect = self.name_surf.get_rect(center = (400, 100))

        pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect)
        pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect,10)
        SCREEN.blit(self.name_surf, self.name_rect)

        pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect)
        pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect,10)



        self.score_message = self.score_font.render(f'Your score: {self.current_time}', False, (64, 64, 64))
        self.score_message_rect = self.score_message.get_rect(center = (400, 300))

        if self.current_time == 0:
            SCREEN.blit(self.instruct_surf, self.instruct_rect)

        else:
            SCREEN.blit(self.score_message, self.score_message_rect)
            
    def update(self):
        self.display_score()
