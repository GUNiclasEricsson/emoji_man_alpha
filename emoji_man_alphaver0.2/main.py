# imports the library/module pygame
import pygame

# imports all variables, functions and classes
from settings import *

from emojienemy import *

from emojiman import *

from gamemap import *

from tiles import Tile1

from scores import Score

# calls the init method to init the modules 
pygame.init()

# the running variable takes the boolean true to be able to use in the while-loop
running = True


# creates an instance of the Clock class for keeping the framerate

clock = pygame.time.Clock() 


sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()


enemy_1 = EmojiEnemy(start_x= 1600, start_y= 800, steps= 450)
enemy_2 = EmojiEnemy(start_x= 1040, start_y= 496, steps= 150)
enemies.add(enemy_1, enemy_2)

score = Score()

player_1 = EmojiMan()
player.add(player_1)
level = GameMap((0, 0), sprites)

#def draw():
#    for r_index, row in enumerate(GAME_MAP):
#                for c_index, col in enumerate(row):
#                    x = c_index * RECT_SIZE
#                    y = r_index * RECT_SIZE
#                    if col == 1:
#                        #print("1")
#                        print(x, y)
#
#    level = GameMap((x, y), sprites)
#    return level

#draw()
sprites.add(player_1, enemy_1, enemy_2)

level.draw_map(sprites)


# while run the main game loop as long as the value is True
while running: 
    # goes trough each event in the .get method from the .event module 
    # they are stored as a (object)?
    for event in pygame.event.get():
        #print(event)
        # checks if the type of event is a key being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == ESC:
                running = False

    SCREEN.blit(BACKGROUND, (0, 0))


    key = pygame.key.get_pressed()
    player.update(key)
    player_1.apply_gravity()

    enemies.update()
    #print(enemies)

    score.current_time()
    score.update()
    
    #level.draw_map(sprites)
    collide = pygame.Rect.colliderect(player_1.rect, enemy_1.rect)
    print(collide)

    if collide:
        print("DIE!", player_1.rect, enemy_1.rect)

    for sprite in sprites:
        #print(sprite.surface, sprite.rect)
        SCREEN.blit(sprite.surface, sprite.rect)

    #sprites.draw(SCREEN)
    #for player in player.sprites():
    #    print(player.rect)
    #    for enemy in enemies.sprites():
    #        print(enemy.rect)





    pygame.display.flip()
    # calls the .tick method an passing the FPS variable as an argument for keeping the framerate locked
    clock.tick(FPS)
                
pygame.quit()



