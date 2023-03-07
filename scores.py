
import pygame

clock = pygame.time.Clock() # Kanske räcker att ha denna i mainloopen?

def display_score():

    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = score_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
  
score = 0

score_font = pygame.font.Font('fonts/RETRO_SPACE.ttf', 50)
