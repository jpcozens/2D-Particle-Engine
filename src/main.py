import pygame
from pygame.locals import *
pygame.init()

import global_state

display = pygame.display.set_mode((1920,1080), pygame.NOFRAME) # noframe flag = borderless window
clock = pygame.time.Clock()

while True:

    global_state.CURRENT_FRAME += 1

    global_state.MOUSE_LMB_DOWN = False
    global_state.MOUSE_LMB_UP = False
    global_state.MOUSE_LMB_PRESSED = pygame.mouse.get_pressed()[0]
    global_state.MOUSE_POS = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: global_state.MOUSE_LMB_DOWN = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: global_state.MOUSE_LMB_UP = True

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
