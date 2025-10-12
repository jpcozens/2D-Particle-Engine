import pygame
from pygame.locals import *
pygame.init()

import global_state

display = pygame.display.set_mode((1920,1080), pygame.NOFRAME) # noframe flag = borderless window
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # debug exit pre-GUI
                pygame.quit()
                exit()

    # update sprite physics
    for sprite_group in global_state.ALL_GROUPS:
        for sprite in sprite_group:
            # call sprite physics update method if it exists
            update_method = getattr(sprite, "update", None)
            if callable(update_method):
                update_method()

    display.fill((75,0,0))

    # render sprites
    for sprite_group in global_state.ALL_GROUPS:
        for sprite in sprite_group:
            display.blit(sprite.surf, sprite.rect)


    pygame.display.update()
    clock.tick(global_state.FPS_MAX)
