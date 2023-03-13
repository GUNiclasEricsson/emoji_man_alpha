import pygame


class Score():
    def __init__(self, start_time = 0, current_time = 0):
        #score_surf = score_font.render('First', False, (64, 64, 64))
        self.start_time = start_time
        self.current_time = current_time
        self.score_font = pygame.font.Font('pygameintro/fonts/RETRO_SPACE.ttf', 50)
        self.instruct_font = pygame.font.Font('pygameintro/fonts/RETRO_SPACE.ttf', 30)

    

    def display_score(self):
        self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        
        self.score_surf = self.score_font.render(f'Score: {self.current_time}', False, (64,64,64))
        self.score_rect = self.score_surf.get_rect (center = (400,50))
        screen.blit(self.score_surf, self.score_rect)

        return self.current_time


    def game_over(self):
        pass

    def update(self):
        self.display_score()
