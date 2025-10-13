import pygame
from pygame.locals import *
pygame.init()

import global_state
from particle.particle_controller import Particle_Controller

# pygame instances
display = pygame.display.set_mode((1920,1080), pygame.NOFRAME) # noframe flag = borderless window
clock = pygame.time.Clock()

# init particle module
Particle_Controller((1920,1080))

while True:

    # debug print FPS to CLI
    if global_state.CURRENT_FRAME % 60 == 0:
        print(global_state.FPS)

    global_state.CURRENT_FRAME += 1
    global_state.MOUSE_LMB_DOWN = False
    global_state.MOUSE_LMB_UP = False
    global_state.MOUSE_LMB_PRESSED = pygame.mouse.get_pressed()[0]
    global_state.MOUSE_POS = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        # update global mouse input
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            global_state.MOUSE_LMB_DOWN = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            global_state.MOUSE_LMB_UP = True

        # debug pre-GUI program exit functionality
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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
    global_state.FPS = round(clock.get_fps(),0)
