import pygame
from pygame.locals import *

"""
Isaac Sutor
PyGame Intro
"""
pygame.init()


screen = pygame.display.set_mode((800, 600))

# Variable to keep main loop running
running = True

# create surface
surf = pygame.Surface((50, 50))
# color surface
surf.fill((255, 255, 255))
rect = surf.get_rect()

# draw rect
screen.blit(surf, (400, 300))
pygame.display.flip()

# Main Loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # check KEYDOWN event;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # check for QUIT
            elif event.type == pygame.QUIT:
                running = False


